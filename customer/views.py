import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from accounts.models import Account

from customer.models import Customer, CustomerAccount, CustomerAddress, FullName

# Create your views here.
def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username1 = request.POST['username']
        email1 = request.POST['email']
        city = request.POST['city']
        country = request.POST['country']
        street = request.POST['street']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if CustomerAccount.objects.filter(username = username1).exists():
                messages.error(request,"Username already taken")
            if Customer.objects.filter(email = email1).exists():
                messages.error(request,"Email already taken")
            else:
                customer_account = CustomerAccount.objects.create(username = username1,password = pass1)
                customer_account.save()

                fullname = FullName.objects.create (first_name = fname,last_name = lname)
                fullname.save()

                customer_address = CustomerAddress.objects.create (city = city,country = country,street=street)
                customer_address.save()

                customer = Customer.objects.create(fullname = fullname,customer_account=customer_account,customer_address=customer_address,email=email1,phone_number=phone)
                customer.save()

                # customer = Customer.objects.create(first_name = fname,last_name=lname,username=username1,email=email1,phone_number=phone,address=address,password=pass1)
                user = Account.objects.create_user(first_name = fname,last_name=lname,email=email1,username=username1,password=pass1)
                user.phone_number = phone
                user.save()
                # customer.save()
                if user is not None:
                    # auth.login(request,customer)
                    messages.success(request,"Register successfully")
                    return render(request,'customer/register.html')              
        else:
            messages.error(request,"Password not match")
    else:
        return render(request,'customer/register.html')

def login(request):
    if request.method == "POST":
        email2 = request.POST.get('email',False)
        password2 = request.POST.get('password',False)

        user = auth.authenticate(email=email2, password=password2)

        if user is not None:
            auth.login(request,user)
            # messages.success(request,'')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            # messages.error(request,email2)
            # messages.error(request,password2)
            return redirect ('login')    

    return render(request,'customer/login.html')

def logout(request):
    auth.logout(request)
    return redirect ('login')
    return       
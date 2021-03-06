# Generated by Django 3.1 on 2022-04-12 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothes', '0001_initial'),
        ('laptop', '0001_initial'),
        ('smartphone', '0001_initial'),
        ('book', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('type',models.CharField(max_length=200,default='book')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhoneItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('weight', models.IntegerField()),
                ('width', models.IntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartphone.smartphone')),
            ],
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='LaptopItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('weight', models.IntegerField()),
                ('width', models.IntegerField()),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptop.laptop')),
            ],
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('clothes_size', models.IntegerField()),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes')),
            ],
            bases=('shop.item',),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.item')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
            bases=('shop.item',),
        ),
    ]

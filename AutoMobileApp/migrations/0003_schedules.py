# Generated by Django 4.2.7 on 2023-12-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMobileApp', '0002_rename_address_customer_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
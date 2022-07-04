# Generated by Django 3.1.4 on 2022-04-26 13:59

import counting_app_user.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phonenumber', models.IntegerField(unique=True, verbose_name='شماره تماس')),
                ('Fname', models.CharField(max_length=150, verbose_name='نام')),
                ('Lname', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('adress', models.CharField(max_length=500, verbose_name='آدرس')),
                ('national_code', models.CharField(max_length=150, verbose_name='کد ملی')),
                ('is_newsletteres', models.BooleanField(default=False, verbose_name='عضویت در خبر نامه')),
                ('day_stamp', models.IntegerField(verbose_name='روز عضویت')),
                ('month_stamp', models.IntegerField(verbose_name='ماه عضویت')),
                ('year_stamp', models.IntegerField(verbose_name='سال عضویت')),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
            },
            managers=[
                ('objects', counting_app_user.managers.UserManager()),
            ],
        ),
    ]

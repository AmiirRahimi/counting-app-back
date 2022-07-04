# Generated by Django 3.1.4 on 2022-04-26 14:03

import counting_app_user.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('counting_app_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Fname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='Lname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='day_stamp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_newsletteres',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='month_stamp',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='national_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='year_stamp',
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phonenumber',
            field=models.IntegerField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[counting_app_user.validators.UnicodePhonenumberValidator()], verbose_name='phonenumber'),
        ),
    ]

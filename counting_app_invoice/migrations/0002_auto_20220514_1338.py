# Generated by Django 3.1.4 on 2022-05-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting_app_invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='final_registration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
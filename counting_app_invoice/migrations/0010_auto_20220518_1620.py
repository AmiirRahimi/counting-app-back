# Generated by Django 3.1.4 on 2022-05-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting_app_invoice', '0009_auto_20220518_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]

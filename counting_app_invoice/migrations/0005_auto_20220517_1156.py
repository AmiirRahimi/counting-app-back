# Generated by Django 3.1.4 on 2022-05-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting_app_invoice', '0004_auto_20220517_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
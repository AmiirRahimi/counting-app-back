# Generated by Django 3.1.4 on 2022-05-12 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counting_app_customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='counting_app_user.customuser'),
            preserve_default=False,
        ),
    ]

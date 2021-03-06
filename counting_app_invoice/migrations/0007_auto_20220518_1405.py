# Generated by Django 3.1.4 on 2022-05-18 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counting_app_cloth', '0003_cloth_seller_or_tailor_name'),
        ('counting_app_invoice', '0006_auto_20220517_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='count',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price',
        ),
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counting_app_cloth.cloth')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counting_app_invoice.invoice')),
            ],
        ),
    ]

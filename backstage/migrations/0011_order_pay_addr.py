# Generated by Django 2.1.7 on 2019-04-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0010_order_order_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pay_addr',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
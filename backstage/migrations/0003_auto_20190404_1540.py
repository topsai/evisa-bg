# Generated by Django 2.1.7 on 2019-04-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0002_auto_20190404_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='airimg1',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='airimg2',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='hotelimg',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='passport_img1',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='passport_img2',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]

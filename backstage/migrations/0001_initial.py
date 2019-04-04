# Generated by Django 2.1.7 on 2019-04-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('passport_img1', models.CharField(max_length=256)),
                ('passport_img2', models.CharField(max_length=256)),
                ('airimg1', models.CharField(max_length=256)),
                ('airimg2', models.CharField(max_length=256)),
                ('hotelimg', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='userdata',
            field=models.ForeignKey(on_delete=True, to='backstage.UserData'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_info',
            field=models.ForeignKey(on_delete=True, to='backstage.OrderInfo'),
        ),
    ]

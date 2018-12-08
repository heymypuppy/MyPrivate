# Generated by Django 2.1.1 on 2018-10-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_addr_handler_basic_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basicTel', models.CharField(max_length=11)),
                ('orderNum', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('orderImg', models.CharField(max_length=30)),
                ('orderType', models.CharField(max_length=20)),
                ('orderStatus', models.CharField(max_length=20)),
                ('orderAcount', models.CharField(max_length=10)),
                ('restTel', models.CharField(max_length=20)),
            ],
        ),
    ]

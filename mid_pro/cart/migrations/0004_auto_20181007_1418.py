# Generated by Django 2.1.1 on 2018-10-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20181007_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='temcountvalue',
            name='dishTotal',
            field=models.IntegerField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='temcountvalue',
            name='dishValue',
            field=models.IntegerField(max_length=50),
        ),
    ]

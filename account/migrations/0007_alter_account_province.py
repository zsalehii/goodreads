# Generated by Django 3.2.8 on 2021-12-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_isscientific'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='province',
            field=models.CharField(default='آذربایجان غربی', max_length=30, null=True),
        ),
    ]

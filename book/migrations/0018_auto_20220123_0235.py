# Generated by Django 3.2.10 on 2022-01-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_auto_20220123_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='read',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='addbook',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addbook',
            name='saved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='addbook',
            name='saved_count',
            field=models.IntegerField(default=0),
        ),
    ]

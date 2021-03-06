# Generated by Django 3.1.2 on 2020-10-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201014_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW'), ('jpy', 'JPY')], default='krw', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean'), ('jp', 'Japanese')], default='krw', max_length=2),
        ),
    ]

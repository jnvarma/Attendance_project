# Generated by Django 4.2 on 2023-06-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(default='default_username', max_length=100),
        ),
    ]

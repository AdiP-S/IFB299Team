# Generated by Django 2.1 on 2018-10-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Employee', 'Employee'), ('Employee', 'Manager')], max_length=50),
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200904_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

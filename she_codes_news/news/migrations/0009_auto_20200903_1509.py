# Generated by Django 3.0.8 on 2020-09-03 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20200903_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsstory',
            old_name='ingredients',
            new_name='main_content',
        ),
        migrations.RemoveField(
            model_name='newsstory',
            name='method',
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-07 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolistitem_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistitem',
            name='content2',
        ),
    ]
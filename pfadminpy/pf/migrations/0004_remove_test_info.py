# Generated by Django 2.2.5 on 2019-09-19 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pf', '0003_test_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='info',
        ),
    ]

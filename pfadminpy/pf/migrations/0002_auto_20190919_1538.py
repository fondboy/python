# Generated by Django 2.2.5 on 2019-09-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='memo',
            field=models.CharField(max_length=40),
        ),
    ]
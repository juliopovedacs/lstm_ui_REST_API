# Generated by Django 2.2.7 on 2019-11-20 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_runningcase_prefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='time',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
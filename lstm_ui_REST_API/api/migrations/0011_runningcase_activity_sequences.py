# Generated by Django 3.0.1 on 2020-01-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200114_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningcase',
            name='activity_sequences',
            field=models.ManyToManyField(to='api.ActivitySequence'),
        ),
    ]
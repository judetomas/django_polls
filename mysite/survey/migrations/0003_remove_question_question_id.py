# Generated by Django 2.2.5 on 2020-04-12 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200411_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_id',
        ),
    ]

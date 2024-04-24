# Generated by Django 3.2.25 on 2024-03-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Speaking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ielts1',
            name='IsOld',
        ),
        migrations.RemoveField(
            model_name='ielts2',
            name='IsOld',
        ),
        migrations.RemoveField(
            model_name='ielts3',
            name='IsOld',
        ),
        migrations.AddField(
            model_name='ielts1topics',
            name='IsOld',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ielts23topics',
            name='IsOld',
            field=models.BooleanField(default=False),
        ),
    ]

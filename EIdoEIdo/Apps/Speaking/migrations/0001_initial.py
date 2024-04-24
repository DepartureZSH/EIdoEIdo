# Generated by Django 3.2.25 on 2024-03-30 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IELTS1Topics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IELTS23Topics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IELTS3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=100)),
                ('IsOld', models.BooleanField()),
                ('Topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Speaking.ielts23topics')),
            ],
        ),
        migrations.CreateModel(
            name='IELTS2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=100)),
                ('Requirement', models.CharField(max_length=500)),
                ('IsOld', models.BooleanField()),
                ('Topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Speaking.ielts23topics')),
            ],
        ),
        migrations.CreateModel(
            name='IELTS1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=100)),
                ('IsOld', models.BooleanField()),
                ('Topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Speaking.ielts1topics')),
            ],
        ),
    ]
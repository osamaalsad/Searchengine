# Generated by Django 3.0.5 on 2020-05-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('URL', models.CharField(max_length=400)),
                ('Dscription', models.TextField()),
            ],
        ),
    ]

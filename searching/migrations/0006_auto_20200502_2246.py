# Generated by Django 3.0.5 on 2020-05-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0005_unkownsearch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unkownsearch',
            name='ID',
            field=models.IntegerField(),
        ),
    ]
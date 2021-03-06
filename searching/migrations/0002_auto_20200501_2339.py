# Generated by Django 3.0.5 on 2020-05-01 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='searchingdata',
            name='ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='searching.Category', verbose_name='Category'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='unlike_count',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2 on 2022-08-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
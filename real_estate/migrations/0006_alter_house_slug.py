# Generated by Django 4.0.4 on 2022-04-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0005_alter_house_address_line_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
    ]

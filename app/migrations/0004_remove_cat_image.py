# Generated by Django 5.0.2 on 2024-02-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cat_breed_alter_cat_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='image',
        ),
    ]

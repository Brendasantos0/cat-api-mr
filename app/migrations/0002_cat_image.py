# Generated by Django 5.0.2 on 2024-02-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='image',
            field=models.ImageField(default='', upload_to='img/cat'),
            preserve_default=False,
        ),
    ]

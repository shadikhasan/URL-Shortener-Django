# Generated by Django 5.0.7 on 2024-07-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]

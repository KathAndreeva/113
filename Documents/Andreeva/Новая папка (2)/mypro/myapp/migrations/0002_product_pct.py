# Generated by Django 4.2.5 on 2024-09-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pct',
            field=models.ImageField(blank=True, upload_to='myapp/static/img'),
        ),
    ]

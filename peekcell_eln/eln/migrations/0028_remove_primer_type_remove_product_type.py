# Generated by Django 5.1.4 on 2024-12-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0027_experimentqpcr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primer',
            name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]

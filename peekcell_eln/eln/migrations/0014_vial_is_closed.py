# Generated by Django 5.1.4 on 2024-12-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0013_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vial',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
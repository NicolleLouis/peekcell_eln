# Generated by Django 5.1.4 on 2024-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0005_sample_vial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='type',
            field=models.CharField(choices=[('blood', 'Blood'), ('urine', 'Urine')], default='urine', max_length=5),
        ),
    ]

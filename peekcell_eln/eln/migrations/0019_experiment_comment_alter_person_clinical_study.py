# Generated by Django 5.1.4 on 2024-12-31 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0018_sample_label_vial_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='comment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='clinical_study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='eln.clinicalstudy'),
        ),
    ]
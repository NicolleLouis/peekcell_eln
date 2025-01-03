# Generated by Django 5.1.4 on 2024-12-24 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0007_storage_person_is_test_sample_storage_vial_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='samples', to='eln.person'),
        ),
        migrations.AlterField(
            model_name='vial',
            name='sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vials', to='eln.sample'),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-27 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0015_vial_created_at_vial_is_sediment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='experiments', to='eln.vial')),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentFilter',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eln.experiment')),
                ('filter_size', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('eln.experiment',),
        ),
    ]

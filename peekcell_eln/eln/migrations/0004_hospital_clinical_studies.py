# Generated by Django 5.1.4 on 2024-12-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0003_hospital_person_clinical_study_person_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='clinical_studies',
            field=models.ManyToManyField(to='eln.clinicalstudy'),
        ),
    ]

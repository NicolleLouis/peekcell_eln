# Generated by Django 5.1.4 on 2024-12-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0022_experimentreversetranscriptase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentreversetranscriptase',
            name='kit',
            field=models.CharField(choices=[('mircury_lna_rt_kit', 'miRCURY LNA RT Kit')], default='mircury_lna_rt_kit', max_length=18),
        ),
        migrations.AlterField(
            model_name='experimentrnaextraction',
            name='kit',
            field=models.CharField(choices=[('urine_microrna_kit', 'Urine miRNA Kit'), ('mirneasy_advanced_mini_kit', 'miRNeasy Advanced Mini Kit'), ('mirneasy_serum_plasma_advanced_kit', 'miRNeasy Serum/Plasma Advanced Kit')], default='mirneasy_serum_plasma_advanced_kit', max_length=34),
        ),
    ]

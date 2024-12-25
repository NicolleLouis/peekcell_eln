# Generated by Django 5.1.4 on 2024-12-25 13:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0011_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('chloroform', 'Chloroform'), ('trizol', 'Trizol'), ('isopropanol', 'Isopropanol'), ('beta_mercaptoethanol', 'Beta-mercaptoethanol'), ('urine_microrna_kit', 'Urine miRNA Kit'), ('mirneasy_advanced_mini_kit', 'miRNeasy Advanced Mini Kit'), ('mirneasy_serum_plasma_advanced_kit', 'miRNeasy Serum/Plasma Advanced Kit'), ('mircury_lna_rt_kit', 'miRCURY LNA RT Kit'), ('mircury_lna_pcr_kit', 'miRCURY LNA PCR Kit'), ('spike_in_kit', 'Spike-in Kit'), ('primer', 'Primer')], default='chloroform', max_length=34),
        ),
    ]

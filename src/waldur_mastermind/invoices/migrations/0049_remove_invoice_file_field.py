# Generated by Django 2.2.13 on 2021-03-01 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0048_fix_slurm_invoice_items'),
    ]

    operations = [
        migrations.RemoveField(model_name='invoice', name='_file',),
    ]

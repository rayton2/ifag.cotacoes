# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ifag', '0008_remove_quotation_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotation',
            options={
                'permissions': (
                    (
                        'can_add_quotation',
                        'Add Quotation'
                    ),
                    (
                        'can_change_approved_quotation',
                        'Change Approved Quotation'
                    )
                ),
                'verbose_name': 'Cotação',
                'verbose_name_plural': 'Cotações'},
        ),
    ]
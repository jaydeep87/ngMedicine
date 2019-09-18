# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-24 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstype',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='businesstype',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='caresidense_subtype_master',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='caresidense_subtype_master',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='healthoholic_subtype_master',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='healthoholic_subtype_master',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='kurable_subtype_master',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='kurable_subtype_master',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='planassign',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='planassign',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='plancategory',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='plancategory',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='createdAt',
            field=models.DateTimeField(blank=True, db_column='createdAt', null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='updatedAt',
            field=models.DateTimeField(blank=True, db_column='updatedAt', null=True),
        ),
    ]

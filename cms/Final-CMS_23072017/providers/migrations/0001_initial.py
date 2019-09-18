# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-20 11:34
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hfu_cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CaResidense_subtype_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=10000)),
                ('delete', models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Healthoholic_subtype_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=10000)),
                ('delete', models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kurable_subtype_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=10000)),
                ('delete', models.BooleanField(default=False, help_text='Deactivate_Kurablesub_Type')),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asked_reviewer', models.BooleanField(default=False)),
                ('revert', models.BooleanField(default=False)),
                ('send_elastic', models.BooleanField(default=False)),
                ('free_text', models.CharField(blank=True, max_length=5000, null=True)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_user', models.IntegerField(null=True)),
                ('free_text', models.TextField(blank=True, max_length=5000, null=True)),
                ('no_of_employee', models.IntegerField(blank=True, null=True)),
                ('plan_name', models.CharField(blank=True, max_length=200, null=True)),
                ('plan_title', models.CharField(blank=True, max_length=200, null=True)),
                ('plan_price', models.FloatField(blank=True, max_length=200, null=True)),
                ('investigation', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('consultation', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('imaging', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('others', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('package_description', models.CharField(max_length=1000, null=True)),
                ('discount_on_plan', models.FloatField(blank=True, null=True)),
                ('price_of_plan_after_discount', models.FloatField(blank=True, max_length=50, null=True)),
                ('plan_validity', models.CharField(blank=True, max_length=100, null=True)),
                ('age_group', models.CharField(blank=True, max_length=50, null=True)),
                ('user_category', models.CharField(blank=True, help_text='gender', max_length=50, null=True)),
                ('instructions', models.CharField(blank=True, max_length=1000, null=True)),
                ('timings', models.TextField(null=True)),
                ('image_url', models.CharField(blank=True, max_length=200, null=True)),
                ('need_review', models.BooleanField(default=True)),
                ('activation_status', models.BooleanField(default=True)),
                ('submission_date', models.DateField(auto_now=True)),
                ('acceptance_date', models.DateField(blank=True, null=True)),
                ('last_updated_date', models.DateTimeField(auto_now_add=True)),
                ('last_reviewed_on', models.DateTimeField(auto_now_add=True)),
                ('service_offered_in_plan', models.CharField(blank=True, max_length=300, null=True)),
                ('working_hours', models.CharField(blank=True, max_length=300, null=True)),
                ('corporate_plan', models.BooleanField(default=False)),
                ('nurse_plan', models.BooleanField(default=False)),
                ('wellness_plan', models.BooleanField(default=False)),
                ('hfues_plan', models.BooleanField(default=False)),
                ('is_home_service', models.BooleanField(default=False)),
                ('is_enterprise_service', models.BooleanField(default=False)),
                ('is_life_service', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=1000, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('kurable_plan_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('healthoholic_plan_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('caresidense_plan_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan_reviewer_name', to=settings.AUTH_USER_MODEL)),
                ('plan_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.PlanCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_user', models.IntegerField(null=True)),
                ('free_text', models.TextField(blank=True, max_length=5000, null=True)),
                ('enterprise_service_provider', models.BooleanField(default=False)),
                ('home_service_provider', models.BooleanField(default=False)),
                ('life_service_provider', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('provider_unique_id', models.CharField(blank=True, default=uuid.uuid4, max_length=200, null=True, unique=True)),
                ('hs_list', models.CharField(blank=True, max_length=1000, null=True)),
                ('ls_list', models.CharField(blank=True, max_length=1000, null=True)),
                ('es_list', models.CharField(blank=True, max_length=1000, null=True)),
                ('organisation_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('years_in_service', models.CharField(blank=True, max_length=200, null=True)),
                ('quality_certification', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('person_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('r_house_door_bldg_no', models.CharField(blank=True, max_length=200, null=True)),
                ('r_street', models.CharField(blank=True, max_length=200, null=True)),
                ('r_location', models.CharField(blank=True, max_length=200, null=True)),
                ('r_city', models.CharField(blank=True, max_length=200, null=True)),
                ('r_state', models.CharField(blank=True, max_length=200, null=True)),
                ('r_zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('r_phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('c_house_door_bldg_no', models.CharField(blank=True, max_length=200, null=True)),
                ('c_street', models.CharField(blank=True, max_length=200, null=True)),
                ('c_location', models.CharField(blank=True, max_length=200, null=True)),
                ('c_city', models.CharField(blank=True, max_length=200, null=True)),
                ('c_state', models.CharField(blank=True, max_length=200, null=True)),
                ('c_zip_code', models.CharField(blank=True, max_length=200, null=True)),
                ('c_phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('beneficiary_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=200, null=True)),
                ('account_no', models.CharField(blank=True, max_length=200, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=200, null=True)),
                ('certification_validity', models.CharField(blank=True, max_length=200, null=True)),
                ('preferred_location', models.CharField(blank=True, max_length=200, null=True)),
                ('tat', models.CharField(blank=True, max_length=500, null=True)),
                ('home_rate_card', models.FileField(null=True, upload_to='rate_card/')),
                ('life_rate_card', models.FileField(null=True, upload_to='rate_card/')),
                ('enterprise_rate_card', models.FileField(null=True, upload_to='rate_card/')),
                ('remarks', models.TextField(null=True)),
                ('createdAt', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedAt', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.BusinessType')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hfu_cms.Stage')),
            ],
            options={
                'ordering': ('organisation_name',),
            },
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.ServiceProvider'),
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='published_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan_publisher_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serviceplan',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hfu_cms.Stage'),
        ),
        migrations.AddField(
            model_name='planassign',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.ServicePlan'),
        ),
        migrations.AddField(
            model_name='planassign',
            name='plan_reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

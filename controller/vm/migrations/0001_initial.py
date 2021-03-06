# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('instance_name', models.TextField(max_length=128, null=True)),
                ('ip_address', models.IPAddressField(null=True)),
                ('hostname', models.CharField(max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstanceTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('type_instances', models.IntegerField(choices=[(1, 'Virturl Machine'), (2, 'Amazon Web Service'), (3, 'Cloud Computing Platform'), (4, 'Google Cloud Platform')], default=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='instance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vm.InstanceTypes'),
        ),
    ]

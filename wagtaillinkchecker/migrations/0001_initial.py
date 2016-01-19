# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePreferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automated_scanning', models.BooleanField(default=False)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
        ),
    ]

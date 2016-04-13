# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 13:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('initialized', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=253)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DomainSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=500)),
                ('incoming', models.BooleanField(default=True)),
                ('auto_delete_message', models.BooleanField(default=False)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.EmailField(max_length=254)),
                ('to', models.EmailField(default='', max_length=254)),
                ('subject', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
                ('message_id', models.CharField(max_length=500)),
                ('cc', models.EmailField(default='', max_length=254)),
                ('bcc', models.EmailField(default='', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('incoming', 'Inbox'), ('outgoing', 'Sent'), ('draft', 'Draft')], max_length=5)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadedView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder', models.IntegerField(default=0)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Domain')),
                ('message', models.ManyToManyField(to='mail.Message')),
            ],
        ),
        migrations.CreateModel(
            name='UrlKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailgun_key', models.CharField(max_length=500)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Domain')),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_cron'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('task', models.CharField(choices=[('S', 'Signup')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

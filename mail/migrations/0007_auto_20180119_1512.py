# Generated by Django 2.0.1 on 2018-01-19 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_auto_20180118_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='mail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mail.Mail'),
        ),
    ]

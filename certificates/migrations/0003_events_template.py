# Generated by Django 2.0 on 2022-12-03 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_auto_20221203_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='certificates.Templates', verbose_name='Template'),
        ),
    ]

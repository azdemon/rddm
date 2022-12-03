# Generated by Django 2.0 on 2022-12-03 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('file', models.FilePathField(verbose_name='File')),
                ('headerfont', models.CharField(max_length=50, verbose_name='Header font')),
                ('headersize', models.CharField(max_length=50, verbose_name='Header size')),
                ('headermtop', models.CharField(max_length=50, verbose_name='Header Margin Top')),
                ('headerln', models.CharField(max_length=50, verbose_name='Header line height')),
                ('textfont', models.CharField(max_length=50, verbose_name='Text font')),
                ('textsize', models.CharField(max_length=50, verbose_name='Text size')),
                ('textmtop', models.CharField(max_length=50, verbose_name='Text Margin Top')),
                ('textln', models.CharField(max_length=50, verbose_name='Text line height')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
        ),
        migrations.AddField(
            model_name='fields',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.Templates', verbose_name='Template'),
        ),
    ]

# Generated by Django 4.0 on 2022-03-29 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'aboutme', 'verbose_name_plural': 'About Me'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'skills', 'verbose_name_plural': 'Skills'},
        ),
    ]

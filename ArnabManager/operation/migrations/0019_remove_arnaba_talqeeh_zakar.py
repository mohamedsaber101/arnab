# Generated by Django 4.2.1 on 2023-07-09 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0018_remove_arnaba_birth_date_arnaba_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arnaba',
            name='talqeeh_zakar',
        ),
    ]
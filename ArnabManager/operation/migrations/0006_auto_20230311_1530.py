# Generated by Django 2.2 on 2023-03-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20230311_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arnaba',
            name='age',
        ),
        migrations.AddField(
            model_name='arnaba',
            name='birth_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='arnaba',
            name='مرات_التلقيح',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='arnaba',
            name='birth_times',
            field=models.IntegerField(default=None),
        ),
    ]

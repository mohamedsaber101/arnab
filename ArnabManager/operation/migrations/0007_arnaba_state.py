# Generated by Django 2.2 on 2023-03-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_auto_20230311_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='arnaba',
            name='state',
            field=models.CharField(default='فاضية', max_length=200),
        ),
    ]

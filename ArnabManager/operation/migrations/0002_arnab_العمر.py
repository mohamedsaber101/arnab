# Generated by Django 2.2 on 2023-03-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arnab',
            name='العمر',
            field=models.CharField(default='NullValue', max_length=200),
            preserve_default=False,
        ),
    ]

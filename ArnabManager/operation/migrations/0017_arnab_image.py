# Generated by Django 4.2.1 on 2023-07-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0016_alter_arnab_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='arnab',
            name='image',
            field=models.CharField(default='arnab.png', max_length=200),
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0010_alter_arnaba_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arnaba',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

# Generated by Django 2.2 on 2023-03-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_arnab_hh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('b_id', models.CharField(max_length=200)),
            ],
        ),
    ]

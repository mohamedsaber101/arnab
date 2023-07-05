# Generated by Django 4.2.1 on 2023-07-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0009_alter_arnaba_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arnaba',
            name='state',
            field=models.CharField(choices=[('فاضية', 'فاضية'), ('مليانة', 'مليانة'), ('متلقحة', 'متلقحة'), ('مرضعة', 'مرضعة'), ('حامل و مرضعة', 'حامل و مرضعة'), ('متلقحة و مرضعة', 'متلقحة و مرضعة')], default='emmm', max_length=200),
        ),
    ]

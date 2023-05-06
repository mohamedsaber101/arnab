# Generated by Django 4.2.1 on 2023-05-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_arnaba_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arnaba',
            name='state',
            field=models.CharField(choices=[('empty', 'فاضية'), ('pregnant', 'مليانة'), ('mated', 'متلقحة'), ('feeding', 'مرضعة'), ('pregnant-feeding', 'حامل ومرضعة'), ('mated-feeding', 'متلقحة ومرضعة')], default='emmm', max_length=200),
        ),
    ]

# Generated by Django 2.2 on 2023-03-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arnaba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('kind', models.CharField(max_length=200)),
                ('birth_times', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Topics',
        ),
        migrations.RemoveField(
            model_name='arnab',
            name='description',
        ),
        migrations.RemoveField(
            model_name='arnab',
            name='hh',
        ),
        migrations.RemoveField(
            model_name='arnab',
            name='wlada_num',
        ),
        migrations.RemoveField(
            model_name='arnab',
            name='العمر',
        ),
        migrations.AddField(
            model_name='arnab',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arnab',
            name='desc',
            field=models.CharField(default='ffgfdgfd', max_length=200),
            preserve_default=False,
        ),
    ]
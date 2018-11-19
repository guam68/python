# Generated by Django 2.1.2 on 2018-11-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=35)),
                ('age', models.IntegerField(blank=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('diagnosis', models.TextField(blank=True)),
                ('contact_name', models.TextField(blank=True, max_length=25)),
                ('contact_number', models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]

# Generated by Django 2.2.27 on 2022-03-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devApp', '0002_auto_20220321_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datepart', models.DateField()),
            ],
        ),
    ]

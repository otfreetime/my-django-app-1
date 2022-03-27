# Generated by Django 2.2.27 on 2022-03-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20220320_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('temperature', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
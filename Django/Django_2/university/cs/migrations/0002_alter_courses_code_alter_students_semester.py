# Generated by Django 4.2.1 on 2023-05-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='semester',
            field=models.IntegerField(),
        ),
    ]

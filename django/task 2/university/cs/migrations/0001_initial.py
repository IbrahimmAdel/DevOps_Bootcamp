# Generated by Django 4.2.1 on 2023-05-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('code', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('l_name', models.CharField(max_length=15)),
                ('semester', models.IntegerField(max_length=2)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
    ]

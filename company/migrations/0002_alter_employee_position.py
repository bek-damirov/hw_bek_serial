# Generated by Django 3.2 on 2022-12-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.IntegerField(),
        ),
    ]
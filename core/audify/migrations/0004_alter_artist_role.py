# Generated by Django 4.2.10 on 2024-02-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audify', '0003_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='role',
            field=models.CharField(choices=[('singer', 'Singer'), ('guitarist', 'Guitarist')], max_length=200),
        ),
    ]

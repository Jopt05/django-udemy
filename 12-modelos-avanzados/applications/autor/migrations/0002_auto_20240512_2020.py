# Generated by Django 3.2.25 on 2024-05-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='appellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='nombre',
            new_name='nombres',
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=50),
        ),
    ]

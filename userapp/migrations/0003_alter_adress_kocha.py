# Generated by Django 4.0.2 on 2022-02-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_client_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='kocha',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

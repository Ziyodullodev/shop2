# Generated by Django 4.0.2 on 2022-02-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_alter_adress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='zipcode',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

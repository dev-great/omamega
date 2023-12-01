# Generated by Django 3.2 on 2023-11-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0005_property_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('Commercial', 'Commercial'), ('Bungalow', 'Bungalow'), ('Duplex', 'Duplex'), ('Mansion', 'Mansion'), ('Terrace', 'Terrace'), ('Penthouse', 'Penthouse')], max_length=15),
        ),
    ]
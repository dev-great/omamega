# Generated by Django 3.2 on 2023-11-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='rental_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

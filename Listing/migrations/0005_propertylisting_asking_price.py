# Generated by Django 3.2 on 2023-11-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listing', '0004_rename_purchase_price_propertylisting_selling_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylisting',
            name='asking_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
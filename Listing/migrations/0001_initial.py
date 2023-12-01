# Generated by Django 3.2 on 2023-11-07 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_published', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Property.property')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
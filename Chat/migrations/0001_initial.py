# Generated by Django 3.2 on 2023-11-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_sent', models.DateTimeField()),
                ('is_read', models.BooleanField()),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]
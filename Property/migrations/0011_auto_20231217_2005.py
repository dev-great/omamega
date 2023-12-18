# Generated by Django 3.2 on 2023-12-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0010_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='plot_location',
            new_name='plot_no',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='plot_size',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

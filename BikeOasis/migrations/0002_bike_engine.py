# Generated by Django 4.2.1 on 2023-08-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BikeOasis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='engine',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
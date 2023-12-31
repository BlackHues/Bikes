# Generated by Django 4.2.1 on 2023-09-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BikeOasis', '0006_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]

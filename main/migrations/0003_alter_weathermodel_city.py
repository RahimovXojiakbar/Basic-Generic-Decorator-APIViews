# Generated by Django 5.1.3 on 2024-12-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_weathermodel_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weathermodel',
            name='city',
            field=models.CharField(max_length=200),
        ),
    ]

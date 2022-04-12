# Generated by Django 3.1.6 on 2021-04-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210422_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Product',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Car', 'Car'), ('Scooter', 'Scooter'), ('Motorcycle', 'Motorcycle')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

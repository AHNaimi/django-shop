# Generated by Django 4.1.4 on 2022-12-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_productmodel_pro_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pro_image',
            field=models.ImageField(upload_to='pro_images'),
        ),
    ]

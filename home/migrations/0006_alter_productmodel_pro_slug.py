# Generated by Django 4.1.4 on 2022-12-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_productmodel_pro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pro_slug',
            field=models.SlugField(unique=True),
        ),
    ]

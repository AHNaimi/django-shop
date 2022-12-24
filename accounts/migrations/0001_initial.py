# Generated by Django 4.1.4 on 2022-12-24 13:09

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, validators=[accounts.models.phone_valid])),
                ('province', models.CharField(choices=[('Alborz Province', 'Alborz Province'), ('Ardabil Province', 'Ardabil Province'), ('Bushehr Province', 'Bushehr Province'), ('Chaharmahal and Bakhtiari Province', 'Chaharmahal and Bakhtiari Province'), ('East Azerbaijan Province', 'East Azerbaijan Province'), ('Isfahan Province', 'Isfahan Province'), ('Fars Province', 'Fars Province'), ('Gilan Province', 'Gilan Province'), ('Golestan Province', 'Golestan Province'), ('Hamadan Province', 'Hamadan Province'), ('Hormozgan Province', 'Hormozgan Province'), ('Ilam Province', 'Ilam Province'), ('Kerman Province', 'Kerman Province'), ('Kermanshah Province', 'Kermanshah Province'), ('Khuzestan Province', 'Khuzestan Province'), ('Kohgiluyeh and Boyer-Ahmad Province', 'Kohgiluyeh and Boyer-Ahmad Province'), ('Kurdistan Province', 'Kurdistan Province'), ('Lorestan Province', 'Lorestan Province'), ('Markazi Province', 'Markazi Province'), ('Mazandaran Province', 'Mazandaran Province'), ('North Khorasan Province', 'North Khorasan Province'), ('Qazvin Province', 'Qazvin Province'), ('Qom Province', 'Qom Province'), ('Razavi Khorasan Province', 'Razavi Khorasan Province'), ('Semnan Province', 'Semnan Province'), ('Sistan and Baluchestan Province', 'Sistan and Baluchestan Province'), ('South Khorasan Province', 'South Khorasan Province'), ('Tehran Province', 'Tehran Province'), ('West Azerbaijan Province', 'West Azerbaijan Province'), ('Yazd Province', 'Yazd Province'), ('Zanjan Province', 'Zanjan Province')], default='Tehran Province', max_length=64)),
                ('address', models.TextField()),
                ('zip_code', models.CharField(max_length=10, validators=[accounts.models.zipcode_valid])),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from accounts.manager import UserManager
from django.db import models


province_choice = (
    ('Alborz Province', 'Alborz Province'), ('Ardabil Province', 'Ardabil Province'), ('Bushehr Province',
                                                                                       'Bushehr Province'),
    ('Chaharmahal and Bakhtiari Province', 'Chaharmahal and Bakhtiari Province'),
    ('East Azerbaijan Province', 'East Azerbaijan Province'), ('Isfahan Province', 'Isfahan Province'),
    ('Fars Province', 'Fars Province'), ('Gilan Province', 'Gilan Province'),
    ('Golestan Province', 'Golestan Province'), ('Hamadan Province', 'Hamadan Province',),
    ('Hormozgan Province', 'Hormozgan Province'), ('Ilam Province', 'Ilam Province'),
    ('Kerman Province', 'Kerman Province'),
    ('Kermanshah Province', 'Kermanshah Province'), ('Khuzestan Province', 'Khuzestan Province'),
    ('Kohgiluyeh and Boyer-Ahmad Province', 'Kohgiluyeh and Boyer-Ahmad Province'),
    ('Kurdistan Province', 'Kurdistan Province'), ('Lorestan Province', 'Lorestan Province'),
    ('Markazi Province', 'Markazi Province'), ('Mazandaran Province', 'Mazandaran Province'),
    ('North Khorasan Province', 'North Khorasan Province'), ('Qazvin Province', 'Qazvin Province'),
    ('Qom Province', 'Qom Province'), ('Razavi Khorasan Province', 'Razavi Khorasan Province'),
    ('Semnan Province', 'Semnan Province'), ('Sistan and Baluchestan Province', 'Sistan and Baluchestan Province'),
    ('South Khorasan Province', 'South Khorasan Province'), ('Tehran Province', 'Tehran Province'),
    ('West Azerbaijan Province', 'West Azerbaijan Province'), ('Yazd Province', 'Yazd Province'),
    ('Zanjan Province', 'Zanjan Province')
)


def phone_valid(value):
    """ a phone number (in iran) must be 11 number """
    if len(value) == 11:
        return value
    else:
        raise ValidationError('phone number is not valid')


def zipcode_valid(value):
    """ zip code must be 10 number(in iran) """
    if len(value) == 10:
        return value
    else:
        raise ValidationError('zipcode is not valid')


class UserModel(AbstractBaseUser, PermissionsMixin):
    """ customizing User model """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, validators=[phone_valid])
    province = models.CharField(max_length=64, choices=province_choice, default='Tehran Province')
    address = models.TextField()
    zip_code = models.CharField(max_length=10, validators=[zipcode_valid])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'province', 'address', 'zip_code']

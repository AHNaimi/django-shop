from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, address, password):

        if not email:
            raise ValueError('user must have email')

        if not first_name:
            raise ValueError('user must have first name')

        if not last_name:
            raise ValueError('please insert last_name')

        if not phone:
            raise ValueError('please insert your phone-number')

        if not address:
            raise ValueError("please insert your address")

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, phone=phone,
                          address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, address, password):
        user = self.create_user(email, first_name, last_name, phone, address, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
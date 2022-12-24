from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ a class for making simple user and superuser """
    def create_user(self, first_name, last_name, email, phone_number, province, address, zip_code, password):
        """ a function that makes simple user that can not go to admin panel"""
        user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                          phone_number=phone_number, province=province, address=address, zip_code=zip_code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number, province, address, zip_code, password):
        """ a function for creating superuser that can go to admin panel and makes change """
        user = self.create_user(first_name=first_name, last_name=last_name,
                                email=self.normalize_email(email), phone_number=phone_number,
                                province=province, address=address, zip_code=zip_code,
                                password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

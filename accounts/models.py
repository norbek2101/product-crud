from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from accounts.manager import CustomUserManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 



class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = PhoneNumberField(db_index=True, unique=True)
    full_name = models.CharField(max_length=250, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
   

    

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"(User ID : {self.id}) {self.phone_number}"


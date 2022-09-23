from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class VansModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    body_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.make + ' ' + self.model or ''




# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#         user.set_password(password)
#         user.save()
#         return user


# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name
#     def get_short_name(self):
#         return self.name
#     def __str__(self):
#         return self.email
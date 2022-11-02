from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import EmployeeManager


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_revokated = models.DateTimeField()

    class Meta:
        abstract = True


class Employee(AbstractBaseUser, PermissionsMixin):
    """
    Model that represents an Employee.
    """
    MANAGEMENT = 'management'
    SALES = 'sales'
    SUPPORT = 'support'

    ROLE = (
        (MANAGEMENT, 'management'),
        (SALES, 'sales'),
        (SUPPORT, 'support')
    )

    username = models.CharField(max_length=30, unique=True, default='username')
    email = models.EmailField(max_length=250, unique=True, default='email@email.com')
    first_name = models.CharField(max_length=100, blank=False, default='first_name')
    last_name = models.CharField(max_length=100, blank=False, default='last_name')
    password = models.CharField(max_length=100, blank=False, default='password')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    department = models.CharField(max_length=10, choices=ROLE)

    objects = EmployeeManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

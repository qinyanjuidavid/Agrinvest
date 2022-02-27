from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext as _


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name_plural = "Tracking Model"


class CustomManager(BaseUserManager):
    def create_user(self, email, username, password=None,
                    role="",
                    is_active=True, is_admin=False,
                    is_staff=False):
        if email is None:
            raise ValueError("Users must have an email!")
        if password is None:
            raise ValueError("Users must have a password!")
        if username is None:
            raise ValueError("Users must have a username!")
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.save(using=self._db)

        return user_obj

    def create_staff(self, email, username, password=None):
        user = self.create_user(
            email, username, password=password,
            is_active=True, is_admin=False,
            is_staff=True
        )
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email, username, password=password,
            is_staff=True, is_admin=True, is_active=True
        )
        return user


class User(AbstractBaseUser, TrackingModel):
    username_validator = UnicodeUsernameValidator()
    role_choice = (
        ("Administrator", "Administrator"),
        ("Customer", "Customer"),
        ("Dealer", "Dealer"),
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': ('A user with that username already exists.')
        }
    )
    full_name = models.CharField(
        _('full name'), max_length=150, blank=True, null=True)
    phone = PhoneNumberField(_('phone number'),
                             unique=True, blank=True,
                             null=True, max_length=27)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
        'unique': ('A user with that email already exists.')
    }
    )
    is_active = models.BooleanField(_("active"), default=True)
    is_admin = models.BooleanField(_("admin"), default=False)
    is_staff = models.BooleanField(_("staff"), default=False)
    role = models.CharField(_("role"), max_length=56, choices=role_choice)
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)

    def __str__(self):
        return self.username

    objects = CustomManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def admin(self):
        return self.admin

    @property
    def staff(self):
        return self.staff

    @property
    def active(self):
        return self.active


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, unique=True)
    bio = models.TextField(_("bio"), blank=True, null=True)
    profile_picture = models.ImageField(
        _("profile picture"), upload_to="picture/%y/%m/%d",
        default="default.png")

    class Meta:
        abstract = True
        ordering = ["-id"]

    def __str__(self):
        return self.user.username


class Administrator(Profile):
    job_id = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Customer(Profile):
    pass

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name_plural = "Customers"
        ordering = ["-id"]
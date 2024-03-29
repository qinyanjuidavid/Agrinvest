# Generated by Django 4.2.7 on 2023-11-10 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "updated_flag",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=3,
                        verbose_name="updated flag",
                    ),
                ),
                (
                    "deleted_flag",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=3,
                        verbose_name="deleted flag",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="deleted at"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="full name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "A user with that email already exists."
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone_no",
                    models.CharField(
                        blank=True,
                        max_length=56,
                        null=True,
                        verbose_name="phone number",
                    ),
                ),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="active"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="superuser"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("SUPERUSER", "SUPERUSER"),
                            ("CUSTOMER", "CUSTOMER"),
                            ("FARMER", "FARMER"),
                        ],
                        default="CUSTOMER",
                        max_length=20,
                        verbose_name="role",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_added_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_deleted_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "users",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="SuperUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(default=-1.286389, verbose_name="latitude"),
                ),
                (
                    "longitude",
                    models.FloatField(default=36.817223, verbose_name="longitude"),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="default.png",
                        null=True,
                        upload_to="profile_images",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="bio"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("P", "Prefer not to say"),
                        ],
                        default="P",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="county"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="town"
                    ),
                ),
                (
                    "estate",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="estate"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="date of birth"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Super Users",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="FarmProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "updated_flag",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=3,
                        verbose_name="updated flag",
                    ),
                ),
                (
                    "deleted_flag",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=3,
                        verbose_name="deleted flag",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="deleted at"
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        max_length=89, unique=True, verbose_name="category"
                    ),
                ),
                (
                    "category_icon",
                    models.ImageField(blank=True, null=True, upload_to="crops_icons/"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_added_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "deleted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_deleted_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Farm Product Categories",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Farmer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(default=-1.286389, verbose_name="latitude"),
                ),
                (
                    "longitude",
                    models.FloatField(default=36.817223, verbose_name="longitude"),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="default.png",
                        null=True,
                        upload_to="profile_images",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="bio"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("P", "Prefer not to say"),
                        ],
                        default="P",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="county"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="town"
                    ),
                ),
                (
                    "estate",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="estate"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="date of birth"
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(default=True, verbose_name="verified"),
                ),
                (
                    "protect_email",
                    models.BooleanField(default=True, verbose_name="protect email"),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("BEGINNER", "BEGINNER"),
                            ("AMATEUR", "AMATEUR"),
                            ("PRO", "PRO"),
                        ],
                        default="BEGINNER",
                        max_length=20,
                        verbose_name="level",
                    ),
                ),
                (
                    "response_time",
                    models.CharField(
                        choices=[
                            ("2 Hrs", "2 Hrs"),
                            ("6 Hrs", "6 Hrs"),
                            ("1 day", "1 day"),
                            ("2+ Days", "2+ Days"),
                        ],
                        default="2 Hrs",
                        max_length=20,
                        verbose_name="response_time",
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="accounts.farmproductcategory",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Farmers",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(default=-1.286389, verbose_name="latitude"),
                ),
                (
                    "longitude",
                    models.FloatField(default=36.817223, verbose_name="longitude"),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="default.png",
                        null=True,
                        upload_to="profile_images",
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=500, null=True, verbose_name="bio"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("P", "Prefer not to say"),
                        ],
                        default="P",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="county"
                    ),
                ),
                (
                    "town",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="town"
                    ),
                ),
                (
                    "estate",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="estate"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="date of birth"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Customers",
                "ordering": ["-id"],
            },
        ),
    ]

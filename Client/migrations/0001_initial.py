# Generated by Django 4.2.7 on 2023-11-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="USER_INFORMATION",
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
                    "picture",
                    models.FileField(
                        upload_to="USER_INFORMATION_Image/", verbose_name="عکس "
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="نام و نام خانوادگی"),
                ),
                (
                    "Email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="ایمیل"
                    ),
                ),
                ("password", models.CharField(max_length=12, verbose_name="رمز کاربر")),
            ],
            options={
                "verbose_name_plural": "اطلاعات کاربران سایت",
                "db_table": "USER_INFORMATION",
            },
        ),
    ]
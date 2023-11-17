# Generated by Django 4.2.7 on 2023-11-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0012_about_website"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact_us",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="نام و نام خانوادگی"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="ایمیل")),
                (
                    "subject",
                    models.CharField(max_length=200, verbose_name="موضوع پیام"),
                ),
                ("message", models.TextField(verbose_name="متن پیام")),
            ],
            options={
                "verbose_name_plural": "ارتباط با ما ",
                "db_table": "Contact_us",
            },
        ),
    ]

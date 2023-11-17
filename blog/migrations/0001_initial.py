# Generated by Django 4.2.7 on 2023-11-14 17:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Client", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category_of_Post",
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
                ("name", models.CharField(max_length=50, verbose_name="اسم دسته بندی")),
                ("slug", models.SlugField(unique=True, verbose_name="آدرس دسته بندی")),
            ],
            options={
                "verbose_name_plural": "دسته بندی های پست ها ",
                "db_table": "Category_of_Post",
            },
        ),
        migrations.CreateModel(
            name="TOTAL_TAGS",
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
                ("name", models.CharField(max_length=50, verbose_name="اسم تگ ")),
                (
                    "slug",
                    models.SlugField(unique=True, verbose_name="آدرس اینترنتی تگ ها "),
                ),
            ],
            options={
                "verbose_name_plural": "تگ های دسته بندی ها ",
                "db_table": "TOTAL_TAGS",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200, verbose_name="عنوان پست ")),
                ("text", ckeditor.fields.RichTextField(verbose_name="متن ")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("P", "منتشر شدن"), ("D", "پیش نویس شدن")],
                        default="D",
                        max_length=1,
                        verbose_name="وضعیت پست ",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Client.user_information",
                        verbose_name="نویسنده",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.category_of_post",
                        verbose_name="دسته بندی مقالات ",
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.total_tags")),
            ],
            options={
                "verbose_name_plural": "پست های نوشته شده ",
                "db_table": "Post",
            },
        ),
    ]

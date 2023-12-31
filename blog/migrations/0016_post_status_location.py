# Generated by Django 4.2.7 on 2023-11-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0015_about_us_model_alter_social_media_website_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="status_location",
            field=models.CharField(
                choices=[
                    ("EDITORS Pick", "منتخب نویسنده"),
                    ("TRENDING POST", "پست برتر"),
                    ("POPULAR POST", "پست محبوب"),
                ],
                max_length=20,
                null=True,
                verbose_name="وضعیت پست از نظر محل",
            ),
        ),
    ]

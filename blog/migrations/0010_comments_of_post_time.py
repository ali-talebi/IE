# Generated by Django 4.2.7 on 2023-11-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_rename_webiste_comments_of_post_website"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments_of_post",
            name="time",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="زمان ساخت"
            ),
        ),
    ]
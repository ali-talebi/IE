# Generated by Django 4.2.7 on 2023-11-15 08:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_alter_comments_webiste"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comments_of_Post",
        ),
    ]

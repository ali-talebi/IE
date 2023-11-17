# Generated by Django 4.2.7 on 2023-11-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Client", "0002_user_information_about_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_information",
            name="face_book",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="فیسبوک"
            ),
        ),
        migrations.AddField(
            model_name="user_information",
            name="github",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="گیت هاب"
            ),
        ),
        migrations.AddField(
            model_name="user_information",
            name="instagram",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="اینستاگرام"
            ),
        ),
        migrations.AddField(
            model_name="user_information",
            name="twitter",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="توئیتر"
            ),
        ),
    ]

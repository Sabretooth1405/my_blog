# Generated by Django 4.1.2 on 2023-02-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]

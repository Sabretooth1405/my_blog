# Generated by Django 4.1.2 on 2023-02-07 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_post_views_view_counter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="view_counter",
            old_name="vies",
            new_name="views",
        ),
    ]

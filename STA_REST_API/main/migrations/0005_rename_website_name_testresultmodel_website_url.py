# Generated by Django 5.0 on 2023-12-21 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_testresultmodel_screenshot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testresultmodel',
            old_name='website_name',
            new_name='website_url',
        ),
    ]

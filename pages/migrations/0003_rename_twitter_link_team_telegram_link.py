# Generated by Django 4.2.3 on 2023-08-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='twitter_link',
            new_name='telegram_link',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-06 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escrowapi', '0004_auto_20210706_0428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ACCOUNT_TYPE',
            new_name='account_type',
        ),
    ]

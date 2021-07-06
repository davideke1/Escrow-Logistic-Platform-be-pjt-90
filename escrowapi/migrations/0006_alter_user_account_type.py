# Generated by Django 3.2.5 on 2021-07-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escrowapi', '0005_rename_account_type_user_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('CUSTOMER', 'CUSTOMER'), ('VENDOR', 'VENDOR')], default=None, max_length=20),
        ),
    ]

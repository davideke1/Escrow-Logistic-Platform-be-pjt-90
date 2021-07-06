# Generated by Django 3.2.5 on 2021-07-06 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=400)),
                ('other_names', models.CharField(blank=True, max_length=400)),
                ('contact', models.CharField(max_length=400)),
                ('gender', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=400)),
                ('vendor_status', models.BooleanField(default=False)),
                ('Customer_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='escrowapi.user')),
                ('first_name', models.CharField(blank=True, max_length=400)),
                ('other_names', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='escrowapi.user')),
                ('business_name', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
    ]

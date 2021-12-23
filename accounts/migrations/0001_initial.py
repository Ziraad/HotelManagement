# Generated by Django 4.0 on 2021-12-22 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, upload_to='media')),
                ('phone_no', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('state', models.CharField(blank=True, max_length=30)),
                ('pin_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(default='0', max_length=11)),
                ('address', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]

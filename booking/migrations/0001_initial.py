# Generated by Django 4.0 on 2021-12-22 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=5)),
                ('room_type', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField(default=1000.0)),
                ('no_of_days_advance', models.IntegerField()),
                ('start_date', models.DateField()),
                ('room_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.roommanager')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('amount', models.FloatField()),
                ('booked_on', models.DateTimeField(auto_now=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.rooms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
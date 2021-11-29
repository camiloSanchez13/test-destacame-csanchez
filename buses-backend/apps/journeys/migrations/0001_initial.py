# Generated by Django 3.1.2 on 2021-11-27 23:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buses', '0001_initial'),
        ('passengers', '0001_initial'),
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journeys', to='buses.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journeys', to='routes.route')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('sale_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='journeys.journey')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='passengers.passenger')),
            ],
        ),
    ]

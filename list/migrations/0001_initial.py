# Generated by Django 3.1.4 on 2020-12-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='Item Name', max_length=30, unique_for_date='date_created')),
                ('quantity', models.CharField(default='Item Quantity', max_length=15)),
                ('item_status', models.CharField(choices=[('BOUGHT', 'Bought'), ('NOT AVAILABLE', 'Unavailable'), ('PENDING', 'Pending')], max_length=13)),
                ('date_created', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0004_alter_health_details_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinments',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='diet',
            name='day',
            field=models.DateField(max_length=7),
        ),
        migrations.AlterField(
            model_name='health_details',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
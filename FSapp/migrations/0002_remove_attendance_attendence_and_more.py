# Generated by Django 4.0.2 on 2022-03-04 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendence',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_status',
            field=models.CharField(choices=[('P', 'PRESENT'), ('A', 'ABSENT')], default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='FSapp.register_details'),
        ),
    ]

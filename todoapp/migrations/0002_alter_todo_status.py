# Generated by Django 5.1.2 on 2024-11-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('c', 'Completed'), ('p', 'Pending')], default='Pending', max_length=1),
        ),
    ]

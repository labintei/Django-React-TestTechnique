# Generated by Django 4.2.13 on 2024-05-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_user_is_active_remove_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

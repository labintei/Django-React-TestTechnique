# Generated by Django 4.2.13 on 2024-05-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_message_chatroom_chatroom_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chatrooms',
            field=models.ManyToManyField(related_name='memberships', to='backend.chatroom'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='bis', to='backend.user'),
        ),
    ]
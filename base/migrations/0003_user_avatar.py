# Generated by Django 5.1.6 on 2025-03-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
    ]

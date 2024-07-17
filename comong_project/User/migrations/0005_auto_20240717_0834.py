# Generated by Django 2.2 on 2024-07-17 08:34

import User.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=15, null=True, unique=True, validators=[User.validators.validate_no_special_characters]),
        ),
    ]

# Generated by Django 3.2.25 on 2024-08-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0015_alter_join_comment_resume_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_comment',
            name='resume_id',
            field=models.URLField(null=True),
        ),
    ]

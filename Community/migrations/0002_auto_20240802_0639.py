# Generated by Django 3.2.25 on 2024-08-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
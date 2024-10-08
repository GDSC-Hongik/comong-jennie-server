# Generated by Django 3.2.25 on 2024-08-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Join_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15, null=True)),
                ('tag', models.CharField(max_length=15, null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('participants_num', models.IntegerField(null=True)),
                ('current_num', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15, null=True)),
                ('tag', models.CharField(max_length=15, null=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('grade', models.IntegerField(null=True)),
                ('sub', models.CharField(max_length=30, null=True)),
                ('profs', models.CharField(max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

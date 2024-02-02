# Generated by Django 5.0.1 on 2024-02-02 12:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('publishedDate', models.DateField()),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('membershipDate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailsID', models.CharField(max_length=50, unique=True)),
                ('numberOfPages', models.IntegerField()),
                ('publisher', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.book', verbose_name='bookID')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowDate', models.DateField()),
                ('returnDate', models.DateField()),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.book', verbose_name='bookID')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.user', verbose_name='userID')),
            ],
        ),
    ]
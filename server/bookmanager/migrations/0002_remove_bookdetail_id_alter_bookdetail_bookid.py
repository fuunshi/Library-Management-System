# Generated by Django 5.0.1 on 2024-02-02 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='bookdetail',
            name='bookID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bookmanager.book', verbose_name='bookID'),
        ),
    ]
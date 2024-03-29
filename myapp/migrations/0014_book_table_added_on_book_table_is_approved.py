# Generated by Django 4.2 on 2024-01-11 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_book_table_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_table',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_table',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]

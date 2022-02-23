# Generated by Django 4.0.1 on 2022-02-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0013_alter_book_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='role',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
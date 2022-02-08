# Generated by Django 4.0.1 on 2022-01-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_remove_book_rating_alter_book_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
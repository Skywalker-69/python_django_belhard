# Generated by Django 4.1.1 on 2022-10-13 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_feedback_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 14, 11, 9, 820113, tzinfo=datetime.timezone.utc), verbose_name='дата публикации'),
        ),
    ]

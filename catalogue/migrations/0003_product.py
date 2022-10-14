# Generated by Django 4.1.1 on 2022-10-12 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Макс. 36 символов', max_length=36, verbose_name='название')),
                ('descr', models.CharField(blank=True, help_text='Макс. 140 символов', max_length=140, null=True, verbose_name='описание')),
                ('article', models.CharField(help_text='Макс. 16 символов', max_length=16, unique=True, verbose_name='Артикль')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Макс. 999999.99', max_digits=8, verbose_name='цена')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='количество')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'app_products',
                'ordering': ('price', 'title', 'article'),
            },
        ),
    ]

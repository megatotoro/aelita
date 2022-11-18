# Generated by Django 4.1.3 on 2022-11-15 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aelitaapp', '0003_alter_doctors_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'db_table': 'categorys',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aelitaapp.categorys', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
                'db_table': 'price',
                'ordering': ['name'],
            },
        ),
    ]

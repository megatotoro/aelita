# Generated by Django 4.1.3 on 2022-11-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aelitaapp', '0004_categorys_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(db_index=True, max_length=300, verbose_name='Название'),
        ),
    ]

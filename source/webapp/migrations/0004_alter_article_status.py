# Generated by Django 4.1.6 on 2023-02-24 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_article_deleted_at_article_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Активна'), ('NOT_ACTIVE', 'Неактивна')], default='ACTIVE', max_length=20, verbose_name='Статус'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(upload_to='', verbose_name='Makale Görseli'),
        ),
    ]

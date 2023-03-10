# Generated by Django 4.1.7 on 2023-02-26 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_article_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Yazan')),
                ('comment_content', models.CharField(max_length=144, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='Makale')),
            ],
        ),
    ]

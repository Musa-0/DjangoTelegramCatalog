# Generated by Django 4.0.5 on 2022-07-19 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0002_delete_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('preview', models.CharField(max_length=500)),
                ('content', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

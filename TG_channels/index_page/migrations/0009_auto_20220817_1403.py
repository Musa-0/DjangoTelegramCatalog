# Generated by Django 3.2.5 on 2022-08-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0008_remove_bots_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_for_chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_categories', models.CharField(max_length=255)),
                ('translit_category', models.CharField(default=None, max_length=255)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='chats',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories_chat', to='index_page.category_for_chats'),
        ),
    ]

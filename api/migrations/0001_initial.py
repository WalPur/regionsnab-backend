# Generated by Django 4.1.3 on 2022-11-07 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('short_desc', models.CharField(max_length=50, verbose_name='Краткое описание')),
                ('full_desc', models.TextField(verbose_name='Полное описание')),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider_image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.news', verbose_name='Новость')),
            ],
        ),
    ]

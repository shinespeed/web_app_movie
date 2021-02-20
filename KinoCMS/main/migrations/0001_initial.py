# Generated by Django 3.1.7 on 2021-02-19 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=250, verbose_name='Name post')),
                ('post_text', models.TextField(verbose_name='Text post')),
                ('post_date_publish', models.DateTimeField(verbose_name='Date publish')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=250, verbose_name='Name post')),
                ('author_name', models.CharField(max_length=50, verbose_name='Name author')),
                ('comment_date_publish', models.DateTimeField(verbose_name='Date publish')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]

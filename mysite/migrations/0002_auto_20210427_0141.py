# Generated by Django 3.2 on 2021-04-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Works',
            new_name='Work',
        ),
    ]

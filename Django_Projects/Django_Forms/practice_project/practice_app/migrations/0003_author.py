# Generated by Django 3.2.9 on 2021-11-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0002_auto_20211125_0412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
        ),
    ]

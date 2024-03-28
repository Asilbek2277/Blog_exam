# Generated by Django 5.0.3 on 2024-03-28 12:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('kasbi', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.TextField()),
                ('sana', models.DateField()),
                ('mavzu', models.TextField()),
                ('matn', models.TextField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.muallif')),
            ],
        ),
    ]

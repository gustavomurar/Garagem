# Generated by Django 5.1.7 on 2025-04-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=80, null=True)),
                ('marca', models.CharField(blank=True, max_length=80, null=True)),
                ('categoria', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('title', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioWeb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('title', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameModel(
            old_name='Portfolio',
            new_name='PortfolioApp',
        ),
    ]
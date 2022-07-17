# Generated by Django 3.2.8 on 2022-07-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('date', models.DateField()),
                ('description', models.TextField(max_length=1555)),
                ('jumlah', models.IntegerField(blank=True, null=True)),
                ('harga', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
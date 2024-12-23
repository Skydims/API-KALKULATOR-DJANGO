# Generated by Django 5.1.4 on 2024-12-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HasilKalkulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angka1', models.FloatField()),
                ('angka2', models.FloatField()),
                ('operator', models.CharField(max_length=10)),
                ('hasil', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

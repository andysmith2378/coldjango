# Generated by Django 4.2.11 on 2024-05-01 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0014_pool_vacancies'),
    ]

    operations = [
        migrations.CreateModel(
            name='SenateRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jacobsladder.pool')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

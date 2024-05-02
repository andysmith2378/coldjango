# Generated by Django 4.2.11 on 2024-05-01 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0012_pool'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='pool',
            constraint=models.UniqueConstraint(fields=('state', 'election'), name='pool_state_and_election'),
        ),
    ]

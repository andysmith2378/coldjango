# Generated by Django 4.2.11 on 2024-04-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0004_lighthouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]

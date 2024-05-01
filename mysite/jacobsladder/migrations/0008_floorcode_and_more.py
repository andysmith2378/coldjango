# Generated by Django 4.2.11 on 2024-04-30 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0007_floor_floor_name_and_lighthouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jacobsladder.floor')),
            ],
        ),
        migrations.AddConstraint(
            model_name='floorcode',
            constraint=models.UniqueConstraint(fields=('number', 'floor'), name='unique_combination_of_number_and_floor'),
        ),
    ]
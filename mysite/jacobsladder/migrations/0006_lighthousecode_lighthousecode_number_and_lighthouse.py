# Generated by Django 4.2.11 on 2024-04-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0005_alter_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LighthouseCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('lighthouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jacobsladder.lighthouse')),
            ],
        ),
        migrations.AddConstraint(
            model_name='lighthousecode',
            constraint=models.UniqueConstraint(fields=('number', 'lighthouse'), name='number_and_lighthouse'),
        ),
    ]
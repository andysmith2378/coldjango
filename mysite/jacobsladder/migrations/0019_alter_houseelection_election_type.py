# Generated by Django 4.2.11 on 2024-05-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0018_housealliance_metaparty_senatealliance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseelection',
            name='election_type',
            field=models.CharField(choices=[('federal', 'Regular'), ('by-election', 'By-Election')], max_length=15),
        ),
    ]

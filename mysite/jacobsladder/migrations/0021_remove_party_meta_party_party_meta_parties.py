# Generated by Django 4.2.11 on 2024-05-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0020_remove_votetally_unique_combination_of_booth_election_and_candidate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='meta_party',
        ),
        migrations.AddField(
            model_name='party',
            name='meta_parties',
            field=models.ManyToManyField(blank=True, to='jacobsladder.metaparty'),
        ),
    ]
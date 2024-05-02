# Generated by Django 4.2.11 on 2024-05-02 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacobsladder', '0015_senateround'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepreference',
            name='source_candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_preference', to='jacobsladder.housecandidate'),
        ),
        migrations.CreateModel(
            name='SenatePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_transferred', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ballot_position', models.PositiveSmallIntegerField(default=0)),
                ('order_elected', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('papers', models.PositiveIntegerField()),
                ('progressive_total', models.PositiveIntegerField()),
                ('transfer_value', models.DecimalField(decimal_places=29, max_digits=31)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_senate', to='jacobsladder.senatecandidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jacobsladder.senateelection')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jacobsladder.senateround')),
                ('source_candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_senate', to='jacobsladder.senatecandidate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
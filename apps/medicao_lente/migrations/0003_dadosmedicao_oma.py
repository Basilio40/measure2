# Generated by Django 3.2.18 on 2023-04-02 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicao_lente', '0002_dadosmedicao_ponte'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosmedicao',
            name='oma',
            field=models.TextField(blank=True, null=True),
        ),
    ]

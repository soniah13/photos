# Generated by Django 5.1.1 on 2024-10-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='tag_category',
            field=models.CharField(choices=[('people', 'People'), ('nature', 'Nature'), ('food', 'Food'), ('animal', 'Animal'), ('lifestyle', 'Lifestyle')], default='nature', max_length=50),
        ),
    ]

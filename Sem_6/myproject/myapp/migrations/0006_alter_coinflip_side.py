# Generated by Django 5.0.1 on 2024-01-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_author_birthday_alter_coinflip_side'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinflip',
            name='side',
            field=models.CharField(default='tail', max_length=5),
        ),
    ]

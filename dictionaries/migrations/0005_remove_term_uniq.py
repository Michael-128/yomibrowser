# Generated by Django 4.2.6 on 2023-10-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0004_alter_term_unique_together_term_uniq'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='term',
            name='uniq',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-24 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='unknown', max_length=255, null=True)),
                ('revision', models.CharField(max_length=255, null=True)),
                ('sequenced', models.BooleanField(default=False, null=True)),
                ('format', models.SmallIntegerField(null=True)),
                ('version', models.SmallIntegerField(null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('url', models.URLField(null=True)),
                ('description', models.TextField(null=True)),
                ('attribution', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=255)),
                ('reading', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('ruleIdentifiers', models.CharField(max_length=255)),
                ('popularity', models.IntegerField()),
                ('definitions', models.TextField()),
                ('sequence', models.IntegerField()),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionaries.dictionary')),
            ],
        ),
    ]

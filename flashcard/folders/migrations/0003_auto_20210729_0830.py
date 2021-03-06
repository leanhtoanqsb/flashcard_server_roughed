# Generated by Django 3.2.5 on 2021-07-29 08:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0002_auto_20210722_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='sets',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folder_owned_sets', to='folders.folder'),
        ),
        migrations.AlterField(
            model_name='word',
            name='sets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_owned_words', to='folders.sets'),
        ),
    ]

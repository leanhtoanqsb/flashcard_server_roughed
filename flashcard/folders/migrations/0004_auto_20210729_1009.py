# Generated by Django 3.2.5 on 2021-07-29 10:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0003_auto_20210729_0830'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='sets',
            name='words',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(default=dict), blank=True, default=[], size=None),
        ),
        migrations.AlterField(
            model_name='sets',
            name='folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_owned_sets', to='folders.folder'),
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word', models.TextField(primary_key=True, serialize=False)),
                ('finded', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedWord',
            fields=[
                ('word_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='twbot1.Word')),
                ('seeked', models.IntegerField(default=0)),
                ('published', models.IntegerField(default=0)),
            ],
            bases=('twbot1.word',),
        ),
        migrations.CreateModel(
            name='TPRI',
            fields=[
                ('tweets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='twbot1.Tweet')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twbot1.Image')),
                ('relatedWords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twbot1.RelatedWord')),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='tweets',
            field=models.ManyToManyField(null=True, to='twbot1.Tweet'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='userr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='twbot1.User'),
        ),
        migrations.AlterUniqueTogether(
            name='tpri',
            unique_together=set([('tweets', 'relatedWords', 'images')]),
        ),
    ]
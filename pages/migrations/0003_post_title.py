# Generated by Django 3.2.9 on 2021-11-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=2, max_length=120),
            preserve_default=False,
        ),
    ]
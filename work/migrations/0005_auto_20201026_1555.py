# Generated by Django 3.1.2 on 2020-10-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20201022_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='backgroundColor',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]

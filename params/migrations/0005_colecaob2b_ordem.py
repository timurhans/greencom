# Generated by Django 2.1.7 on 2020-06-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0004_auto_20200613_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='colecaob2b',
            name='ordem',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]

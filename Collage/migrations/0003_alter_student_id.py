# Generated by Django 4.2 on 2023-06-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collage', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

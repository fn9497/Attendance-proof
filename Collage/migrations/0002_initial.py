# Generated by Django 4.2 on 2023-05-22 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Collage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.course'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='course_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.courseinstance'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.department'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='head_of_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.teacher'),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.course'),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.department'),
        ),
        migrations.AddField(
            model_name='courseinstance',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collage.teacher'),
        ),
    ]

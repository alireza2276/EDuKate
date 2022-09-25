# Generated by Django 4.1.1 on 2022-09-25 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_course_status'),
        ('blog', '0003_alter_blog_datetime_created_alter_blog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='courses.teacher', verbose_name='author'),
        ),
    ]
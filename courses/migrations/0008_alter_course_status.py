# Generated by Django 4.1.1 on 2022-09-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.BooleanField(default='True'),
        ),
    ]

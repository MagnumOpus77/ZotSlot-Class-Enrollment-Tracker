# Generated by Django 4.0.5 on 2022-07-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_room2_course_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room2',
            name='course_codes',
            field=models.CharField(default='', max_length=8),
        ),
    ]

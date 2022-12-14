# Generated by Django 4.0.5 on 2022-07-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_room_delete_room2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]

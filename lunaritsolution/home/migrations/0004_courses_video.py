# Generated by Django 5.0.6 on 2024-09-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_enrollstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='video',
            field=models.FileField(default='null', upload_to='courseVideo/'),
        ),
    ]

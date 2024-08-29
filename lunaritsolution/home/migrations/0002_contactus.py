# Generated by Django 5.0.6 on 2024-07-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
# Generated by Django 5.1.3 on 2024-12-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]

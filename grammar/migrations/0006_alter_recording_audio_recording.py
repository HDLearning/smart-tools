# Generated by Django 3.2 on 2022-10-14 18:47

from django.db import migrations, models
import grammar.models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0005_alter_recording_audio_recording'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='audio_recording',
            field=models.FileField(upload_to=grammar.models.upload_location_activity_images),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='record',
            name='divison',
        ),
        migrations.RemoveField(
            model_name='record',
            name='phone',
        ),
        migrations.AddField(
            model_name='record',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
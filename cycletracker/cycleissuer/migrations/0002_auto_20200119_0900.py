# Generated by Django 3.0.2 on 2020-01-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycleissuer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='SapId',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
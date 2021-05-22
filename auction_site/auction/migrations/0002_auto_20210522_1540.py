# Generated by Django 3.2.3 on 2021-05-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='min_bid',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='time_starting',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
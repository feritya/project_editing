# Generated by Django 4.1.7 on 2023-03-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_user_favorite_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='arac_foto_1',
            field=models.ImageField(default='exit', upload_to='car_fotolari/%Y/%m/'),
            preserve_default=False,
        ),
    ]

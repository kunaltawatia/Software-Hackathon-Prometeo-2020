# Generated by Django 3.0 on 2020-01-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20200126_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='certificate',
            field=models.ImageField(default='default.jpg', upload_to='certificate/'),
        ),
    ]

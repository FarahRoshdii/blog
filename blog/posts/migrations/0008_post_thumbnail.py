# Generated by Django 3.0.8 on 2020-07-04 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200704_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='test', upload_to=''),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usermodel_iduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='lessonsmax',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='iduser',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

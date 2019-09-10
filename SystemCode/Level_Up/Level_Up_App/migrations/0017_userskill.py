# Generated by Django 2.2.4 on 2019-09-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Level_Up_App', '0016_auto_20190908_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(default=None, max_length=256)),
                ('skill2', models.CharField(default=None, max_length=256)),
                ('skill3', models.CharField(default=None, max_length=256)),
                ('skill4', models.CharField(default=None, max_length=256)),
                ('skill5', models.CharField(default=None, max_length=256)),
                ('skill6', models.CharField(default=None, max_length=256)),
                ('skill7', models.CharField(default=None, max_length=256)),
                ('skill8', models.CharField(default=None, max_length=256)),
                ('skill9', models.CharField(default=None, max_length=256)),
                ('skill10', models.CharField(default=None, max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Level_Up_App.User')),
            ],
        ),
    ]
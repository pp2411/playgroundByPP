# Generated by Django 3.2.2 on 2021-05-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PresenceSummarizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img', models.ImageField(upload_to='images/')),
                ('vid', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='timestamps',
            name='case',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='TimeStamps',
        ),
    ]

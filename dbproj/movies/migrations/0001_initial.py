# Generated by Django 5.0.4 on 2024-04-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/')),
                ('actor', models.ImageField(upload_to='')),
                ('actress', models.ImageField(upload_to='')),
                ('priority', models.IntegerField()),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default=1)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-16 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='assignee',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.RESTRICT, to='web.person'),
            preserve_default=False,
        ),
    ]

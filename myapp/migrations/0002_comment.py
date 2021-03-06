# Generated by Django 2.2 on 2019-05-11 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_contents', models.CharField(max_length=400)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.Board')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]

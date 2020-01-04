# Generated by Django 2.0.6 on 2020-01-04 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('depart', '0003_auto_20200104_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.FileField(upload_to=['/home/ami/Desktop/FYPS/FYP/media'])),
                ('technology', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('member_1', models.CharField(max_length=100)),
                ('member_2', models.CharField(max_length=100)),
                ('member_3', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=50)),
                ('hosted_link', models.URLField(blank=True, max_length=128, unique=True)),
                ('stored_on', models.DateTimeField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstore', to='depart.Department')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstore', to='depart.School')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectstore', to='depart.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=['/home/ami/Desktop/FYPS/FYP/media']),
        ),
        migrations.AddField(
            model_name='comments',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='depart.ProjectStore'),
        ),
        migrations.AddField(
            model_name='comments',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
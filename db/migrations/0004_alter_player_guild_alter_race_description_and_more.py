# Generated by Django 4.0.2 on 2024-08-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_skill_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='db.guild'),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.race'),
        ),
    ]
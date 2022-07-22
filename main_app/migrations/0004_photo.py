# Generated by Django 4.0.6 on 2022-07-22 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_agent_alter_treatment_options_bug_agents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bug')),
            ],
        ),
    ]

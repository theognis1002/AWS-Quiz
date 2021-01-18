# Generated by Django 3.1.5 on 2021-01-18 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_type', models.CharField(choices=[('describe_service', 'describe_service'), ('choose_service', 'choose_service'), ('billing', 'billing'), ('general', 'general')], max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('describe_service', 'describe_service'), ('choose_service', 'choose_service'), ('billing', 'billing'), ('general', 'general')], max_length=255)),
                ('question', models.TextField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.answers')),
            ],
        ),
    ]

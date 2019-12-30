# Generated by Django 2.1.5 on 2019-12-30 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='action',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]

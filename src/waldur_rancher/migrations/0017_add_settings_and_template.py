# Generated by Django 2.2.10 on 2020-02-28 10:10

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models

import waldur_core.core.fields
import waldur_core.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0010_customer_geolocation'),
        ('waldur_rancher', '0016_namespace'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='settings',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='+',
                to='structure.ServiceSettings',
            ),
        ),
        migrations.AddField(
            model_name='cluster',
            name='settings',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='+',
                to='structure.ServiceSettings',
            ),
        ),
        migrations.AddField(
            model_name='namespace',
            name='settings',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='+',
                to='structure.ServiceSettings',
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='settings',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='+',
                to='structure.ServiceSettings',
            ),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        blank=True, max_length=500, verbose_name='description'
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=150,
                        validators=[waldur_core.core.validators.validate_name],
                        verbose_name='name',
                    ),
                ),
                ('icon_url', models.URLField(blank=True, verbose_name='icon url')),
                ('uuid', waldur_core.core.fields.UUIDField()),
                (
                    'runtime_state',
                    models.CharField(
                        blank=True, max_length=150, verbose_name='runtime state'
                    ),
                ),
                ('backend_id', models.CharField(blank=True, max_length=255)),
                ('project_url', models.URLField(blank=True)),
                ('default_version', models.CharField(max_length=255)),
                (
                    'versions',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=None
                    ),
                ),
                (
                    'catalog',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='waldur_rancher.Catalog',
                    ),
                ),
                (
                    'cluster',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='waldur_rancher.Cluster',
                    ),
                ),
                (
                    'project',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='waldur_rancher.Project',
                    ),
                ),
                (
                    'settings',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='+',
                        to='structure.ServiceSettings',
                    ),
                ),
            ],
            options={'abstract': False, 'ordering': ('name',)},
        ),
    ]

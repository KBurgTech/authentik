# Generated by Django 2.1.4 on 2018-12-10 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passbook_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthSource',
            fields=[
                ('source_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.Source')),
                ('provider_type', models.CharField(max_length=255)),
                ('request_token_url', models.CharField(blank=True, max_length=255)),
                ('authorization_url', models.CharField(max_length=255)),
                ('access_token_url', models.CharField(max_length=255)),
                ('profile_url', models.CharField(max_length=255)),
                ('consumer_key', models.TextField()),
                ('consumer_secret', models.TextField()),
            ],
            options={
                'verbose_name': 'OAuth Source',
                'verbose_name_plural': 'OAuth Sources',
            },
            bases=('passbook_core.source',),
        ),
        migrations.CreateModel(
            name='UserOAuthSourceConnection',
            fields=[
                ('usersourceconnection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.UserSourceConnection')),
                ('identifier', models.CharField(max_length=255)),
                ('access_token', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'User OAuth Source Connection',
                'verbose_name_plural': 'User OAuth Source Connections',
            },
            bases=('passbook_core.usersourceconnection',),
        ),
    ]

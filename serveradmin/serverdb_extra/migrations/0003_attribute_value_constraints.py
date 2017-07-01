# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('serverdb_extra', '0002_server_indexing')]
    operations = [
        migrations.RunSQL(
            'ALTER TABLE server '
            'ADD CONSTRAINT server_hostname_check '
            r"   CHECK (hostname ~ '\A([a-z0-9]+[\.\-])*[a-z0-9]+\Z')"
        ),
        migrations.RunSQL(
            'ALTER TABLE servertype_attribute '
            'ADD CONSTRAINT servertype_attribute_default_value_check '
            "   CHECK (default_value != '')"
        ),
        migrations.RunSQL(
            'ALTER TABLE server_string_attribute '
            'ADD CONSTRAINT server_string_attribute_value_check '
            "   CHECK (value != '')"
        ),
    ]

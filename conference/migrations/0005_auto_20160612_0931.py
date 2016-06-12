# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_auto_20160612_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='company',
            new_name='representative',
        ),
    ]

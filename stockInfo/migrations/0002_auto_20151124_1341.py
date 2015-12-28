# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZzImsiSisae',
            fields=[
                ('id', models.FloatField(serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=8)),
                ('currentprice', models.IntegerField(null=True, db_column='currentPrice', blank=True)),
                ('netchange', models.FloatField(null=True, db_column='netChange', blank=True)),
                ('tradingvolume', models.IntegerField(null=True, db_column='tradingVolume', blank=True)),
                ('tradingsum', models.BigIntegerField(null=True, db_column='tradingSum', blank=True)),
                ('openprice', models.IntegerField(null=True, db_column='openPrice', blank=True)),
                ('highestprice', models.IntegerField(null=True, db_column='highestPrice', blank=True)),
                ('lowestprice', models.IntegerField(null=True, db_column='lowestPrice', blank=True)),
                ('marketcap', models.BigIntegerField(null=True, db_column='marketCap', blank=True)),
                ('sharesoutstanding', models.IntegerField(null=True, db_column='sharesOutstanding', blank=True)),
                ('eps', models.IntegerField(null=True, db_column='EPS', blank=True)),
                ('per', models.FloatField(null=True, db_column='PER', blank=True)),
                ('bps', models.IntegerField(null=True, db_column='BPS', blank=True)),
                ('pbr', models.FloatField(null=True, db_column='PBR', blank=True)),
                ('dividendamount', models.IntegerField(null=True, db_column='dividendAmount', blank=True)),
                ('dividendpercent', models.FloatField(null=True, db_column='dividendPercent', blank=True)),
                ('designated', models.CharField(max_length=5, null=True, blank=True)),
                ('foreignholdingstock', models.IntegerField(null=True, db_column='foreignHoldingStock', blank=True)),
                ('foreignlimitstock', models.IntegerField(null=True, db_column='foreignLimitStock', blank=True)),
                ('shortvolume', models.IntegerField(null=True, db_column='shortVolume', blank=True)),
                ('shortnotional', models.IntegerField(null=True, db_column='shortNotional', blank=True)),
            ],
            options={
                'db_table': 'zz_imsi_sisae',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='stockinfo',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='stocksisae',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='stocksisae',
            unique_together=set([('code', 'date')]),
        ),
    ]

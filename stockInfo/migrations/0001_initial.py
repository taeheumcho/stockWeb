# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CcData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=8)),
                ('value', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cc_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DataInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('sitecode', models.CharField(max_length=45)),
                ('unit', models.CharField(max_length=10, null=True, blank=True)),
                ('ccy_cd', models.CharField(max_length=45, null=True, blank=True)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'data_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
                ('quarter', models.IntegerField()),
                ('sales', models.IntegerField(null=True, blank=True)),
                ('operatingprofit', models.IntegerField(null=True, db_column='operatingProfit', blank=True)),
                ('profitcontioperpt', models.IntegerField(null=True, db_column='profitContiOperPT', blank=True)),
                ('netincome', models.IntegerField(null=True, db_column='netIncome', blank=True)),
                ('ownernetincome', models.IntegerField(null=True, db_column='ownerNetIncome', blank=True)),
                ('ncontrolnetincome', models.IntegerField(null=True, db_column='nControlNetIncome', blank=True)),
                ('totalasset', models.IntegerField(null=True, db_column='totalAsset', blank=True)),
                ('totalliabilities', models.IntegerField(null=True, db_column='totalLiabilities', blank=True)),
                ('totalequity', models.IntegerField(null=True, db_column='totalEquity', blank=True)),
                ('ownerequity', models.IntegerField(null=True, db_column='ownerEquity', blank=True)),
                ('noncontrollingequity', models.IntegerField(null=True, db_column='nonControllingEquity', blank=True)),
                ('issuedcapital', models.IntegerField(null=True, db_column='issuedCapital', blank=True)),
                ('operactcf', models.IntegerField(null=True, db_column='operActCF', blank=True)),
                ('investactcf', models.CharField(max_length=45, null=True, db_column='InvestActCF', blank=True)),
                ('finactcf', models.CharField(max_length=45, null=True, db_column='finActCF', blank=True)),
                ('capex', models.CharField(max_length=45, null=True, db_column='CAPEX', blank=True)),
                ('fcf', models.CharField(max_length=45, null=True, db_column='FCF', blank=True)),
                ('accruedliability', models.CharField(max_length=45, null=True, db_column='accruedLiability', blank=True)),
                ('ros', models.FloatField(null=True, db_column='ROS', blank=True)),
                ('netprofitratio', models.FloatField(null=True, db_column='netProfitRatio', blank=True)),
                ('roe', models.FloatField(null=True, db_column='ROE', blank=True)),
                ('roa', models.FloatField(null=True, db_column='ROA', blank=True)),
                ('debtratio', models.CharField(max_length=45, null=True, db_column='debtRatio', blank=True)),
                ('reserveratio', models.FloatField(null=True, db_column='reserveRatio', blank=True)),
                ('eps', models.CharField(max_length=45, null=True, db_column='EPS', blank=True)),
                ('per', models.FloatField(null=True, db_column='PER', blank=True)),
                ('pbr', models.FloatField(null=True, db_column='PBR', blank=True)),
                ('bps', models.CharField(max_length=45, null=True, db_column='BPS', blank=True)),
                ('divpershare', models.CharField(max_length=45, null=True, db_column='divPerShare', blank=True)),
                ('divyield', models.CharField(max_length=45, null=True, db_column='divYield', blank=True)),
                ('divipayoutratio', models.CharField(max_length=45, null=True, db_column='diviPayoutRatio', blank=True)),
                ('outstandingshares', models.IntegerField(null=True, db_column='outstandingShares', blank=True)),
            ],
            options={
                'db_table': 'fs_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('siteName', models.CharField(max_length=45, db_column='siteName')),
                ('unit', models.CharField(max_length=45, null=True, blank=True)),
                ('ccy_cd', models.CharField(max_length=45, null=True, blank=True)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'fs_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GicsInfo',
            fields=[
                ('code', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('gicsname', models.CharField(max_length=100, null=True, db_column='gicsName', blank=True)),
                ('gicsname_kr', models.CharField(max_length=100, null=True, db_column='gicsName_kr', blank=True)),
                ('type', models.CharField(max_length=5, null=True, blank=True)),
            ],
            options={
                'db_table': 'gics_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=8)),
                ('value', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'index_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexInfo',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('countrycode', models.CharField(max_length=10, null=True, db_column='countryCode', blank=True)),
            ],
            options={
                'db_table': 'index_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndicatorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=45)),
                ('underlyingCode', models.CharField(max_length=45, db_column='underlyingCode')),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField(null=True, db_column='CREATED_AT', blank=True)),
                ('updated_at', models.DateTimeField(null=True, db_column='UPDATED_AT', blank=True)),
            ],
            options={
                'db_table': 'indicator_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndicatorInfo',
            fields=[
                ('code', models.CharField(max_length=55, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('yn', models.CharField(max_length=45, null=True, db_column='YN', blank=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.DateTimeField(null=True, db_column='CREATED_AT', blank=True)),
                ('updated_at', models.DateTimeField(null=True, db_column='UPDATED_AT', blank=True)),
            ],
            options={
                'db_table': 'indicator_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvestorInfo',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('type', models.CharField(max_length=5, null=True, blank=True)),
                ('num', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'investor_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('dataname', models.CharField(max_length=45)),
                ('yn', models.CharField(max_length=1, db_column='YN')),
                ('sitecode', models.CharField(max_length=10)),
                ('xpath', models.CharField(max_length=255)),
                ('arraynum', models.IntegerField()),
                ('datatype', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'site_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('sitename', models.CharField(max_length=45, null=True, blank=True)),
                ('url1', models.CharField(max_length=255, null=True, blank=True)),
                ('url2', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'site_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('dt', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=4)),
                ('current_price1', models.IntegerField()),
                ('volume', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'stock_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('code', models.CharField(max_length=45, serialize=False, primary_key=True, db_column='CODE')),
                ('ticker', models.CharField(max_length=45, db_column='TICKER')),
                ('market', models.CharField(max_length=45, db_column='MARKET')),
                ('krxcode', models.CharField(max_length=45, null=True, db_column='KRXCODE', blank=True)),
                ('name', models.CharField(max_length=45, null=True, db_column='NAME', blank=True)),
                ('countrycode', models.CharField(max_length=5, null=True, db_column='COUNTRYCODE', blank=True)),
                ('gics', models.CharField(max_length=10, null=True, db_column='GICS', blank=True)),
                ('status', models.CharField(max_length=10, null=True, db_column='STATUS', blank=True)),
                ('create_at', models.DateTimeField(null=True, db_column='CREATE_AT', blank=True)),
                ('update_at', models.DateTimeField(null=True, db_column='UPDATE_AT', blank=True)),
            ],
            options={
                'db_table': 'stock_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockInvestor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=8)),
                ('investorCode', models.CharField(max_length=45, db_column='investorCode')),
                ('buyvolume', models.IntegerField(null=True, db_column='buyVolume', blank=True)),
                ('sellvolume', models.IntegerField(null=True, db_column='sellVolume', blank=True)),
                ('netvolume', models.IntegerField(null=True, db_column='netVolume', blank=True)),
                ('buyamount', models.BigIntegerField(null=True, db_column='buyAmount', blank=True)),
                ('sellamount', models.BigIntegerField(null=True, db_column='sellAmount', blank=True)),
                ('netamount', models.BigIntegerField(null=True, db_column='netAmount', blank=True)),
            ],
            options={
                'db_table': 'stock_investor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StockSisae',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=50, primary_key = True)),
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
                'db_table': 'stock_sisae',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StockTrader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=45)),
                ('date', models.CharField(max_length=8)),
                ('traderCode', models.CharField(max_length=45, db_column='traderCode')),
                ('sellvolume', models.IntegerField(null=True, db_column='sellVolume', blank=True)),
                ('buyvolume', models.IntegerField(null=True, db_column='buyVolume', blank=True)),
                ('sellamount', models.BigIntegerField(null=True, db_column='sellAmount', blank=True)),
                ('buyamount', models.BigIntegerField(null=True, db_column='buyAmount', blank=True)),
            ],
            options={
                'db_table': 'stock_trader',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TraderInfo',
            fields=[
                ('code', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True, blank=True)),
                ('foreigner', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'trader_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='XpathInfo',
            fields=[
                ('code', models.CharField(max_length=30, serialize=False, primary_key=True, db_column='CODE')),
                ('xpath', models.CharField(max_length=100, null=True, db_column='XPATH', blank=True)),
                ('yn', models.IntegerField(null=True, db_column='YN', blank=True)),
                ('description', models.CharField(max_length=100, null=True, db_column='DESCRIPTION', blank=True)),
                ('created_at', models.DateTimeField(null=True, db_column='CREATED_AT', blank=True)),
                ('updated_at', models.DateTimeField(null=True, db_column='UPDATED_AT', blank=True)),
            ],
            options={
                'db_table': 'xpath_info',
                'managed': False,
            },
        ),
    ]

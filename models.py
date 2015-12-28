# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CcData(models.Model):
    code = models.CharField(max_length=45)
    date = models.CharField(max_length=8)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_data'
        unique_together = (('code', 'date'),)


class DataInfo(models.Model):
    code = models.CharField(max_length=45)
    sitecode = models.CharField(max_length=45)
    unit = models.CharField(max_length=10, blank=True, null=True)
    ccy_cd = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_info'
        unique_together = (('code', 'sitecode'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FsData(models.Model):
    code = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    year = models.IntegerField()
    quarter = models.IntegerField()
    sales = models.IntegerField(blank=True, null=True)
    operatingprofit = models.IntegerField(db_column='operatingProfit', blank=True, null=True)  # Field name made lowercase.
    profitcontioperpt = models.IntegerField(db_column='profitContiOperPT', blank=True, null=True)  # Field name made lowercase.
    netincome = models.IntegerField(db_column='netIncome', blank=True, null=True)  # Field name made lowercase.
    ownernetincome = models.IntegerField(db_column='ownerNetIncome', blank=True, null=True)  # Field name made lowercase.
    ncontrolnetincome = models.IntegerField(db_column='nControlNetIncome', blank=True, null=True)  # Field name made lowercase.
    totalasset = models.IntegerField(db_column='totalAsset', blank=True, null=True)  # Field name made lowercase.
    totalliabilities = models.IntegerField(db_column='totalLiabilities', blank=True, null=True)  # Field name made lowercase.
    totalequity = models.IntegerField(db_column='totalEquity', blank=True, null=True)  # Field name made lowercase.
    ownerequity = models.IntegerField(db_column='ownerEquity', blank=True, null=True)  # Field name made lowercase.
    noncontrollingequity = models.IntegerField(db_column='nonControllingEquity', blank=True, null=True)  # Field name made lowercase.
    issuedcapital = models.IntegerField(db_column='issuedCapital', blank=True, null=True)  # Field name made lowercase.
    operactcf = models.IntegerField(db_column='operActCF', blank=True, null=True)  # Field name made lowercase.
    investactcf = models.CharField(db_column='InvestActCF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    finactcf = models.CharField(db_column='finActCF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    capex = models.CharField(db_column='CAPEX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fcf = models.CharField(db_column='FCF', max_length=45, blank=True, null=True)  # Field name made lowercase.
    accruedliability = models.CharField(db_column='accruedLiability', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ros = models.FloatField(db_column='ROS', blank=True, null=True)  # Field name made lowercase.
    netprofitratio = models.FloatField(db_column='netProfitRatio', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    roa = models.FloatField(db_column='ROA', blank=True, null=True)  # Field name made lowercase.
    debtratio = models.CharField(db_column='debtRatio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reserveratio = models.FloatField(db_column='reserveRatio', blank=True, null=True)  # Field name made lowercase.
    eps = models.CharField(db_column='EPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(db_column='PER', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    bps = models.CharField(db_column='BPS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    divpershare = models.CharField(db_column='divPerShare', max_length=45, blank=True, null=True)  # Field name made lowercase.
    divyield = models.CharField(db_column='divYield', max_length=45, blank=True, null=True)  # Field name made lowercase.
    divipayoutratio = models.CharField(db_column='diviPayoutRatio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    outstandingshares = models.IntegerField(db_column='outstandingShares', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fs_data'
        unique_together = (('code', 'date', 'year', 'quarter'),)


class FsInfo(models.Model):
    code = models.CharField(max_length=45)
    sitename = models.CharField(db_column='siteName', max_length=45)  # Field name made lowercase.
    unit = models.CharField(max_length=45, blank=True, null=True)
    ccy_cd = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fs_info'
        unique_together = (('code', 'siteName'),)


class GicsInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=6)
    gicsname = models.CharField(db_column='gicsName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gicsname_kr = models.CharField(db_column='gicsName_kr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gics_info'


class IndexData(models.Model):
    code = models.CharField(max_length=45)
    date = models.CharField(max_length=8)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_data'
        unique_together = (('code', 'date'),)


class IndexInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=45, blank=True, null=True)
    countrycode = models.CharField(db_column='countryCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'index_info'


class IndicatorData(models.Model):
    date = models.CharField(max_length=11)
    code = models.CharField(max_length=45)
    underlyingcode = models.CharField(db_column='underlyingCode', max_length=45)  # Field name made lowercase.
    value = models.FloatField()
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indicator_data'
        unique_together = (('date', 'code', 'underlyingCode'),)


class IndicatorInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=55)
    name = models.CharField(max_length=255, blank=True, null=True)
    yn = models.CharField(db_column='YN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indicator_info'


class InvestorInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investor_info'


class SiteData(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    dataname = models.CharField(max_length=45)
    yn = models.CharField(db_column='YN', max_length=1)  # Field name made lowercase.
    sitecode = models.CharField(max_length=10)
    xpath = models.CharField(max_length=255)
    arraynum = models.IntegerField()
    datatype = models.CharField(max_length=5)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_data'


class SiteInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    sitename = models.CharField(max_length=45, blank=True, null=True)
    url1 = models.CharField(max_length=255, blank=True, null=True)
    url2 = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_info'


class StockData(models.Model):
    code = models.CharField(max_length=45)
    dt = models.CharField(max_length=8)
    time = models.CharField(max_length=4)
    current_price1 = models.IntegerField()
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_data'
        unique_together = (('code', 'dt', 'time'),)


class StockInfo(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=45)  # Field name made lowercase.
    ticker = models.CharField(db_column='TICKER', max_length=45)  # Field name made lowercase.
    market = models.CharField(db_column='MARKET', max_length=45)  # Field name made lowercase.
    krxcode = models.CharField(db_column='KRXCODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gics = models.CharField(db_column='GICS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_at = models.DateTimeField(db_column='CREATE_AT', blank=True, null=True)  # Field name made lowercase.
    update_at = models.DateTimeField(db_column='UPDATE_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_info'


class StockInvestor(models.Model):
    code = models.CharField(max_length=50)
    date = models.CharField(max_length=8)
    investorcode = models.CharField(db_column='investorCode', max_length=45)  # Field name made lowercase.
    buyvolume = models.IntegerField(db_column='buyVolume', blank=True, null=True)  # Field name made lowercase.
    sellvolume = models.IntegerField(db_column='sellVolume', blank=True, null=True)  # Field name made lowercase.
    netvolume = models.IntegerField(db_column='netVolume', blank=True, null=True)  # Field name made lowercase.
    buyamount = models.BigIntegerField(db_column='buyAmount', blank=True, null=True)  # Field name made lowercase.
    sellamount = models.BigIntegerField(db_column='sellAmount', blank=True, null=True)  # Field name made lowercase.
    netamount = models.BigIntegerField(db_column='netAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_investor'
        unique_together = (('code', 'date', 'investorCode'),)


class StockSisae(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=50)
    date = models.CharField(max_length=8)
    currentprice = models.IntegerField(db_column='currentPrice', blank=True, null=True)  # Field name made lowercase.
    netchange = models.FloatField(db_column='netChange', blank=True, null=True)  # Field name made lowercase.
    tradingvolume = models.IntegerField(db_column='tradingVolume', blank=True, null=True)  # Field name made lowercase.
    tradingsum = models.BigIntegerField(db_column='tradingSum', blank=True, null=True)  # Field name made lowercase.
    openprice = models.IntegerField(db_column='openPrice', blank=True, null=True)  # Field name made lowercase.
    highestprice = models.IntegerField(db_column='highestPrice', blank=True, null=True)  # Field name made lowercase.
    lowestprice = models.IntegerField(db_column='lowestPrice', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='marketCap', blank=True, null=True)  # Field name made lowercase.
    sharesoutstanding = models.IntegerField(db_column='sharesOutstanding', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(db_column='PER', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    dividendamount = models.IntegerField(db_column='dividendAmount', blank=True, null=True)  # Field name made lowercase.
    dividendpercent = models.FloatField(db_column='dividendPercent', blank=True, null=True)  # Field name made lowercase.
    designated = models.CharField(max_length=5, blank=True, null=True)
    foreignholdingstock = models.IntegerField(db_column='foreignHoldingStock', blank=True, null=True)  # Field name made lowercase.
    foreignlimitstock = models.IntegerField(db_column='foreignLimitStock', blank=True, null=True)  # Field name made lowercase.
    shortvolume = models.IntegerField(db_column='shortVolume', blank=True, null=True)  # Field name made lowercase.
    shortnotional = models.IntegerField(db_column='shortNotional', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_sisae'
        unique_together = (('code', 'date'),)


class StockTrader(models.Model):
    code = models.CharField(max_length=45)
    date = models.CharField(max_length=8)
    tradercode = models.CharField(db_column='traderCode', max_length=45)  # Field name made lowercase.
    sellvolume = models.IntegerField(db_column='sellVolume', blank=True, null=True)  # Field name made lowercase.
    buyvolume = models.IntegerField(db_column='buyVolume', blank=True, null=True)  # Field name made lowercase.
    sellamount = models.BigIntegerField(db_column='sellAmount', blank=True, null=True)  # Field name made lowercase.
    buyamount = models.BigIntegerField(db_column='buyAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_trader'
        unique_together = (('code', 'date', 'traderCode'),)


class TraderInfo(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=45, blank=True, null=True)
    foreigner = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trader_info'


class XpathInfo(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=30)  # Field name made lowercase.
    xpath = models.CharField(db_column='XPATH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    yn = models.IntegerField(db_column='YN', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xpath_info'


class ZzImsiSisae(models.Model):
    id = models.FloatField(primary_key=True)
    code = models.CharField(max_length=50)
    date = models.CharField(max_length=8)
    currentprice = models.IntegerField(db_column='currentPrice', blank=True, null=True)  # Field name made lowercase.
    netchange = models.FloatField(db_column='netChange', blank=True, null=True)  # Field name made lowercase.
    tradingvolume = models.IntegerField(db_column='tradingVolume', blank=True, null=True)  # Field name made lowercase.
    tradingsum = models.BigIntegerField(db_column='tradingSum', blank=True, null=True)  # Field name made lowercase.
    openprice = models.IntegerField(db_column='openPrice', blank=True, null=True)  # Field name made lowercase.
    highestprice = models.IntegerField(db_column='highestPrice', blank=True, null=True)  # Field name made lowercase.
    lowestprice = models.IntegerField(db_column='lowestPrice', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='marketCap', blank=True, null=True)  # Field name made lowercase.
    sharesoutstanding = models.IntegerField(db_column='sharesOutstanding', blank=True, null=True)  # Field name made lowercase.
    eps = models.IntegerField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(db_column='PER', blank=True, null=True)  # Field name made lowercase.
    bps = models.IntegerField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    dividendamount = models.IntegerField(db_column='dividendAmount', blank=True, null=True)  # Field name made lowercase.
    dividendpercent = models.FloatField(db_column='dividendPercent', blank=True, null=True)  # Field name made lowercase.
    designated = models.CharField(max_length=5, blank=True, null=True)
    foreignholdingstock = models.IntegerField(db_column='foreignHoldingStock', blank=True, null=True)  # Field name made lowercase.
    foreignlimitstock = models.IntegerField(db_column='foreignLimitStock', blank=True, null=True)  # Field name made lowercase.
    shortvolume = models.IntegerField(db_column='shortVolume', blank=True, null=True)  # Field name made lowercase.
    shortnotional = models.IntegerField(db_column='shortNotional', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zz_imsi_sisae'

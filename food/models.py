# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Departments(models.Model):
#     departmentid = models.IntegerField(db_column='DepartmentId', primary_key=True)  # Field name made lowercase.
#     departmentname = models.CharField(db_column='DepartmentName', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Departments'


# class Employees(models.Model):
#     employeeid = models.OneToOneField('self', models.DO_NOTHING, db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
#     employeename = models.CharField(db_column='EmployeeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     dateofjoining = models.DateField(db_column='DateOfJoining', blank=True, null=True)  # Field name made lowercase.
#     photofilename = models.CharField(db_column='PhotoFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Employees'

class Departments(models.Model):
    DepartmentId = models.IntegerField(db_column='DepartmentId', primary_key=True)  # Field name made lowercase.
    DepartmentName = models.CharField(db_column='DepartmentName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departments'


class Employees(models.Model):
    EmployeeId = models.OneToOneField('self', models.DO_NOTHING, db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    EmployeeName = models.CharField(db_column='EmployeeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    Department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.
    DateOfJoining = models.DateField(db_column='DateOfJoining', blank=True, null=True)  # Field name made lowercase.
    PhotoFileName = models.CharField(db_column='PhotoFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Facilitymaster(models.Model):
    facilityid = models.IntegerField(db_column='FacilityID', primary_key=True)  # Field name made lowercase.
    internalorexternal = models.CharField(db_column='InternalOrExternal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    possibletoexpand = models.CharField(db_column='PossibleToExpand', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacilityMaster$'


class Orders(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=10, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Skumasterlist(models.Model):
    skunumber = models.CharField(db_column='SKUNumber', primary_key=True, max_length=50)  # Field name made lowercase.
    skudescription = models.CharField(db_column='SKUDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    therapeuticarea = models.CharField(db_column='TherapeuticArea', max_length=10, blank=True, null=True)  # Field name made lowercase.
    materialtype = models.CharField(db_column='MaterialType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    storagerequirement = models.CharField(db_column='StorageRequirement', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storageloadunit = models.CharField(db_column='StorageLoadUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salesunitofmeasureuom = models.CharField(db_column='SalesUnitOfMeasureUOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    priceperuom = models.FloatField(db_column='PricePerUOM', blank=True, null=True)  # Field name made lowercase.
    uompercase = models.CharField(db_column='UOMPerCase', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uomperpallet = models.CharField(db_column='UOMPerPallet', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SKUMasterList$'


class Truckdetail(models.Model):
    truckid = models.CharField(db_column='TruckID', primary_key=True, max_length=50)  # Field name made lowercase.
    truckdescription = models.CharField(db_column='TruckDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.
    truckbrandid = models.ForeignKey('Truckrefbrands', models.DO_NOTHING, db_column='TruckBrandID', blank=True, null=True)  # Field name made lowercase.
    truckcolor = models.CharField(db_column='TruckColor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TruckDetail'


class Truckrefbrands(models.Model):
    truckrefbrandid = models.IntegerField(db_column='TruckRefBrandID', primary_key=True)  # Field name made lowercase.
    truckrefbrandname = models.CharField(db_column='TruckRefBrandName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TruckRefBrands'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    level_col = models.CharField(max_length=50, blank=True, null=True)
    cvss = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    vulnerability = models.CharField(max_length=50, blank=True, null=True)
    solution = models.CharField(max_length=50, blank=True, null=True)
    reference_col = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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

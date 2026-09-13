# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class Attendance(models.Model):

    rowid = models.IntegerField(primary_key=True)

    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid')

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'attendance'





class AuthGroup(models.Model):

    name = models.CharField(unique=True, max_length=150)



    class Meta:

        managed = False

        db_table = 'auth_group'





class AuthGroupPermissions(models.Model):

    id = models.BigAutoField(primary_key=True)

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

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    email = models.CharField(max_length=254)

    is_staff = models.BooleanField()

    is_active = models.BooleanField()

    date_joined = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'auth_user'





class AuthUserGroups(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_groups'

        unique_together = (('user', 'group'),)





class AuthUserUserPermissions(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'auth_user_user_permissions'

        unique_together = (('user', 'permission'),)





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

    id = models.BigAutoField(primary_key=True)

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





class Events(models.Model):

    eventid = models.IntegerField(primary_key=True)

    eventname = models.CharField(max_length=250, blank=True, null=True)

    eventaddress = models.CharField(max_length=250, blank=True, null=True)

    eventcap = models.IntegerField(blank=True, null=True)

    eventexp = models.IntegerField(blank=True, null=True)

    hobbyid = models.ForeignKey('Hobbies', models.DO_NOTHING, db_column='hobbyid', blank=True, null=True)

    eventattendance = models.ForeignKey(Attendance, models.DO_NOTHING, db_column='eventattendance')

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'events'





class Hobbies(models.Model):

    hobbyid = models.IntegerField(primary_key=True)

    hobbyname = models.CharField(max_length=150)

    hobbycat = models.CharField(max_length=100)



    class Meta:

        managed = False

        db_table = 'hobbies'





class Matchfindr(models.Model):

    rowid = models.IntegerField(primary_key=True)

    hobbyid = models.ForeignKey(Hobbies, models.DO_NOTHING, db_column='hobbyid')

    userexp = models.IntegerField()

    userdesexp = models.IntegerField()

    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)



    class Meta:

        managed = False

        db_table = 'matchfindr'





class Members(models.Model):

    created = models.DateTimeField()



    class Meta:

        managed = False

        db_table = 'members'





class Users(models.Model):

    fname = models.CharField(max_length=100, blank=True, null=True)

    lname = models.CharField(max_length=200, blank=True, null=True)

    age = models.IntegerField()

    username = models.CharField(max_length=150)

    bio = models.CharField(max_length=512, blank=True, null=True)

    city = models.CharField(max_length=90, blank=True, null=True)

    userid = models.CharField(primary_key=True, max_length=50)



    class Meta:

        managed = False

        db_table = 'users'


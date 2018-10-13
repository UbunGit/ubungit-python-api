#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Michael Liao'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField,IntegerField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

'''用户'''
class USER(Model):
    __table__ = 'USERS'

    userID = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    userName = StringField(ddl='varchar(25)')
    passWord = StringField(ddl='varchar(50)')
    phone = StringField(ddl='varchar(11)')
    email = StringField(ddl='varchar(25)')
    wxOpenid = StringField(ddl='varchar(64)')
    status = StringField(ddl='varchar(4)')
    permissions = StringField(ddl='varchar(32)')
    headImage = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time() * 1000)

'''功能'''
class FUNCTION(Model):
    __table__ = 'FUNCTION'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(25)')
    fatherid = StringField(ddl='varchar(50)')
    icon = StringField(ddl='varchar(20)')
    api = StringField(ddl='varchar(50)')
    permissions = IntegerField()

'''权限'''
class PERMISSIONS(Model):

    __table__ = 'PERMISSIONS'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(25)')
    permissions = IntegerField()

'''商品分类'''
class GOODSCATEGORY(Model):

    __table__ = 'GOODSCATEGORY'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(25)')
    fatherid = StringField(ddl='varchar(50)')
    icon = StringField(ddl='varchar(20)')
    depth = IntegerField()

class ATTRIBUTENAME(Model):

    __table__ = 'ATTRIBUTENAME'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(25)')





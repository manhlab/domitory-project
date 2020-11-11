# -*- coding: utf-8 -*-

from sqlalchemy import Column
from app import db1, db2

class User(db1.Model):
    #
    # id = ...
    #
    __tablename__ = 'users'
    __bind_key__  = 'test1' # read from database 'test1'


# SHOULD use different sqlalchemy engine
# otherwise, it will cause 
#
# sqlalchemy.exc.InvalidRequestError: Table 'users' is already 
# defined for this MetaData instance.  Specify 'extend_existing=True'
# to redefine options and columns on an existing Table object.
#
class AnotherUser(db2.Model): 
    #
    # id = ...
    #
    __tablename__ = 'users'
    __bind_key__  = 'test2' # read from database 'test1'
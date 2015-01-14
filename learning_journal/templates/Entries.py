__author__ = 'DarcyElizabeth'
#! usr/bin/env python
# -*- coding: utf-8 -*-

#It should be stored in a database table called entries
#It should have a primary key field called id
#It should have a title field which accepts unicode text up to 255 characters in length
#****The title should be unique and it should be impossible to save an entry without a title.
#***It should have a body field which accepts unicode text of any length (including none)
#****It should have a created field which stores the date and time the object was created.
#****It should have an edited field which stores the date and time the object was last edited.
#****Both the created and edited field should default to now if not provided when a new instance
#is constructed.
#The entry class should support a classmethod all that returns all the entries in the database, ordered so that the most recent entry is first.
#The entry class should support a classmethod by_id that returns a single entry, given an id.

import sqlalchemy as sa

class Entry(Base):
	"""define a data model for the learning journal"""
	__tablename__ = 'Entries'
    id = sa.Column(integer, primary_key = True)
	title = sa.Column(Unicode(255),nullable = False, unique = True)
	body_text = sa.Column(Unicode(None),nullable = False length = None)
	date_created = sa.Column(Datetime())
    date_ edited = sa.Column(Datetime())
    Index('my_index', MyModel.name, unique=True, mysql_length=255)

	def all():
    """returns all entries in order"""
	    q = DBSession.query(Entry)
		q = q.order_by(Entry.date_created)
	        return q

	def by_id():
    """returns a single entry by id"""
	    k = DBSession.query(Entry.id)
		return k



	__table_args__ = ('title', 'body', 'created', 'edited')
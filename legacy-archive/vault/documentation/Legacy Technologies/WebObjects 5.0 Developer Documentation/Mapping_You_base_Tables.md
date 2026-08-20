---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/EnterpriseObjects/Mapping_You_base_Tables.html
archived_at: '2026-07-15T08:15:04.806653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](What_Is_an__ise_Object_.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](WebObjects__ise_Objects.md)

## Mapping Your Enterprise Objects to Database Tables

Enterprise objects make use of a separate file, known as a __model__,
to specify a mapping between tables in the database and your classes
of enterprise objects. This is formally called an __entity-relationship__ (E-R)
model. You use the EOModeler application to create and maintain
these models. With EOModeler you can

- read the
  data dictionary from a database to create a default model, which
  can then be tailored to suit the needs of your application
- specify enterprise object classes for the tables in your database
- specify relationships between enterprise objects and referential
  integrity rules for these relationships
- generate source code files for the enterprise object classes
  you specify
- define fetch specifications (queries) that you can invoke
  by name in your applications
- create and delete databases and database tables

A model represents a level of abstraction above the database.
The database-to-objects mapping embodied in a model sets up a correspondence
between database tables and enterprise objects classes; frequently,
database rows map to instances of the appropriate class as shown
in [Figure 3-2](#apple-ijauescgivdeg).

__Figure
3-2 Mapping between an enterprise object
class and a single table__

![[image: ../Art/DbToEO.gif]](../Art/DbToEO.gif)

In actual practice, the mapping is more flexible than this.
For example:

- You can map
  an enterprise object class to a single table, a subset of a table,
  or to more than one table. For instance, a Person object can get
  its first and last names from a PERSON table but get its street
  address, city, state and zip code from an ADDRESS table.
- Generally an enterprise object instance variable maps to a
  single column, but the column-to-instance variable correspondence
  is similarly flexible. You can map an instance variable to a derived
  column, such as "price \* discount" or "salary \* 12".
- You can map an enterprise object class inheritance hierarchy
  to one or more database tables.

In addition to mapping tables to enterprise object classes
and database columns to instance variables, WebObjects maps database
primary and foreign keys to relationships between objects. WebObjects
defines two types of relationships-to-ones and to-manys-which
are both illustrated in [Figure 3-3](#apple-ijauessjircum). The relationship a MovieRole has to its Movie is
a to-one relationship, while the relationship a Movie has to its
MovieRoles is a to-many.

__Figure
3-3 Mapping relationships__

![[image: ../Art/MapRelations.gif]](../Art/MapRelations.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](What_Is_an__ise_Object_.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](WebObjects__ise_Objects.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

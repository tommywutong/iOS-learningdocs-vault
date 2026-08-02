---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DatabaseBasics/Database_Structure.html
archived_at: '2026-07-15T08:12:52.717627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Database_Basics.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Relationship.md)

## Database Structure

A modern database closely follows the object-oriented paradigm.
The basic unit of organization is the __table__,
which defines the attributes of a data entity. A table can have
zero or more rows.

### Tables

The table is the equivalent of a class definition. It defines
the attributes or properties that each __row__ in
it has. Each property is called a __column__.

Much like in Java, in most databases there are certain primitive
types—like string, int, or double in Java—and each column on
a table is defined to be of a given one of these types. Enterprise
Objects handles the conversion from database internal types to Java
types. Further, for each column, you can declare whether a given
row is required to provide a value or whether it is allowed to be `null`.

You can think of a table as a class, columns as instance variables,
and rows as individual object instances. Like a class definition
file in Java, a table itself does not have variables. You must add
a row to it to use any of its properties.

### Rows

A row is the equivalent of an instance of a Java class. Where
the table is like a class, a row is like an instance of a class.

#### Uniquing

Each row in a given table has to be different in some way
from the others. This is so the database system knows which row
to update or delete when you make changes to your data.

The database uses a __primary key__ that defines
a property (or set of properties) whose value uniquely identifies
each row. For each table you define, you provide a key (or list
of keys), which define how the database system can be sure two given
rows are different. For example, if you are defining a table to
contain data about people, you might decide to use a person's
last name to differentiate each row from the others.

The database system ensures that each row has a unique value
in the column (or combination of values in the set of columns) you
specify as the primary key. Enterprise Objects hides many of the
complexities of database interaction, including the conversion from
database internal types to Java types. However, if you try to override
it and set a value in a row that conflicts with a value in another
row, the database refuses to make the change and reports an error
that your application should handle.

It's important to choose the primary keys for your tables
carefully. If you define your unique key as the column containing
a person's last name, you could run into difficulty as soon as
you try to add two people with the same last name to your table.
In general, it's best to make your primary key one you don't
plan on using for anything else and let Enterprise Objects handle
it for you.

In the example Authors database (see ["Creating the Authors Database"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/iThe_Authors_Application.html)),
each table has a column that servers as its primary key called _ENTITYNAME__ID
of type integer.

#### Not Null

You may wish to declare that without certain data, a row isn't
valid. By declaring a given column not-null, you tell the database
system to reject any new rows that don't provide the required
data.

If you're gathering information for an email mailing list,
for example, a row without a value for the EMAIL_ADDRESS column
isn't useful.

A table's primary key column must always be declared not-null.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Database_Basics.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Relationship.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

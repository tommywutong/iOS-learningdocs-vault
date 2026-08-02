---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DatabaseBasics/Relationship.html
archived_at: '2026-07-15T08:12:52.744007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Database_Structure.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFArchitecture/index.html)

## Relationship

Part of a database's scheme is each table's relationships
with other tables. Each relationship has source and destination
keys that define it.

Rows and tables can relate in many ways. Just as with object-oriented
programming, the way you design your database tables is depends
on how you intend to use them. Relationships can model ownership,
where one row is a subordinate part of another row, but placed in
a separate table for organization—for example, each row in a PERSON
table can _own_ a row in an ADDRESS table because
every person must have a mailing address. Relationships can be optional
or required. In the Authors database, every book must have an author,
but it is conceivable that some authors are as yet unpublished (and
hence would have no rows in the BOOK table).

Since a relationship leads from a source table to a destination
table, we speak of _following_ a relationship.
While Enterprise Objects removes most database considerations from
using your object's relationships, it's useful to understand
how a relationship is maintained at the database level.

Relationships are followed not from table to table but from
a specific row into another row. It doesn't make any sense to
ask what the author of the BOOK table is, but each row of the BOOK
table has a corresponding row in the AUTHOR table.

To link table rows, __foreign keys__ are used.
Foreign keys are columns in the source table whose rows point to
the primary key column in the target table. For example, the BOOK table
has a foreign key column (AUTHOR_ID) that is used to find the corresponding
row in the AUTHOR table (the author of the book). AUTHOR_ID in the
BOOK table does not provide any information on a book. Its only
purpose is to link the rows of the BOOK table with rows on the AUTHOR
table.

One important attribute of a relationship is called ordinality.
Ordinality is a measure of whether a relationship necessarily relates
a row to only one other row, or to multiple rows in the destination
table. This breaks relationships into two types: __to-one__ or __to-many__.

### To-One Relationships

A to-one relationship, as the name suggests, is one where
the source row is connected to only one other row by the relationship.
Each row in the BOOK table has only one author in the AUTHOR table.

The destination column (or columns) of a to-one relationship
must be the same as the primary key columns of the destination table.
This guarantees that there is only one destination row for any given
source row.

To find the row corresponding to a specific book's author,
you would perform the following steps:

1. Get the source
   and destination columns.

   According to the definition of the
   relationship, the source column is AUTHOR_ID in the BOOK table,
   and the destination column is AUTHOR_ID in the AUTHOR table.
2. Get the value in the source row's AUTHOR_ID column.
3. Find the target row in the AUTHOR table (the row whose AUTHOR_ID
   column is equal to the value of the AUTHOR_ID column in the source
   row).

   Since AUTHOR_ID is the primary key for the AUTHOR table,
   there is only one matching row. This row contains data about the
   book's author.

### To-Many Relationships

Alternatively, a relationship can have the ability to connect
the source row with multiple destination rows. For example, in the
Authors database, each author can have multiple books. Remember
that the AUTHOR_ID column in the BOOK table is a foreign key, not
a primary key. Therefore, that column doesn't have to have unique
values throughout the rows of the BOOK table.

To find the BOOK rows corresponding to an AUTHOR row, you
would perform the following steps:

1. Get the source
   and destination columns.

   According to the definition of the
   relationship, the source column is AUTHOR_ID in the
   AUTHOR table, and the destination attribute is AUTHOR_ID in the
   BOOK table.
2. Get the value in the row's AUTHOR_ID column for the source
   row.
3. Find the rows in the BOOK table whose AUTHOR_ID column's
   value is equal to the value from the AUTHOR_ID column in the source
   row.

   Notice that AUTHOR_ID is not the primary key for the BOOK
   table. This means that the relationship could lead to more than
   one row in the BOOK table. Each of these would have the same value
   in their AUTHOR_ID column, meaning that the books that they represent
   have all been written by the same author.

   Further, there's
   no guarantee that there would be any rows in the BOOK table whose AUTHOR_ID
   column's value match the value of the AUTHOR_ID column in the source
   row at all. So the relationship could lead to no rows in the BOOK
   table.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Database_Structure.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFArchitecture/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

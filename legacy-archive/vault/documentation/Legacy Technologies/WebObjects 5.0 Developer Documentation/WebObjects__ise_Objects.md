---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/EnterpriseObjects/WebObjects__ise_Objects.html
archived_at: '2026-07-15T08:15:07.167537Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Mapping_You_base_Tables.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](The_Enterpr_s_Advantage.md)

## WebObjects Support for Enterprise Objects

After your program has accumulated changes to enterprise objects,
WebObjects analyzes the objects for changes, generates corresponding
database operations, and executes those operations to synchronize
the database with in-memory enterprise objects. WebObjects has mechanisms
for ensuring that the integrity of your data is maintained between
your application and the database without sacrificing performance
or flexibility:

**Validation**
: A good part of your application's business logic is
usually validation-for example, verifying that customers don't
exceed their credit limits, return dates don't come before their
corresponding check-out dates, and so on. In your enterprise object
classes, you implement methods that check for invalid data, and
WebObjects automatically invokes them before saving anything to
the database.

**Referential integrity enforcement**
: In your model you can specify rules governing the relationships
between objects, such as whether a to-one relationship is optional
or mandatory. You can also specify delete rules-actions that should
occur when an enterprise object is deleted. For example, if you
have a "department" object you can specify that when it is deleted
all the employees in that department are also deleted (a cascading
delete), all the employees in that department are updated to have
no department (nullify), or the department deletion is rejected
if it has any employees (deny).

**Automatic primary and foreign key generation**
: You needn't maintain database artifacts such as database
primary and foreign key values in your application; WebObjects keeps
track of them for you. Database primary and foreign keys aren't
usually meaningful parts of a business model; rather, they're
attributes created in a relational database to express relationships
between entities. Key values can be generated and propagated automatically.

**Transaction management**
: Most transactions are handled for you, using the native
transaction management features of your database to group database
operations that correspond to the changes that have been made to
enterprise objects in memory. You don't have to worry about beginning,
committing, or rolling back transactions unless you want to fine-tune
transaction management behavior. WebObjects also provides a separate
in-memory transaction management feature that allows you to create
nested contexts in which a child context's changes are folded
into the parent context only upon successful completion of an in-memory
operation.

**Locking**
: WebObjects offers three types of locking. "Pessimistic"
uses your database server's native locking mechanism to lock rows
as they're fetched and prevents update conflicts by never allowing
two users to look at the same object at the same time. "Optimistic"
doesn't detect update conflicts until you try to save an object's
changes to the database; if the corresponding database row has changed
since it was originally fetched, the save is aborted. "On-Demand"
is a mixture of the other two: it locks an object after you fetch
it but before you attempt to modify it. The lock can fail for one
of two reasons: either the corresponding database row has changed
since you fetched the object (optimistic locking), or because someone
else already has a lock on the row (pessimistic locking).

**Faulting**
: When WebObjects fetches an object, it creates objects
representing the destinations of the fetched object's relationships.
By default WebObjects doesn't immediately fetch data for the destination
objects of relationships, however. Fetching is fairly expensive,
and further, if WebObjects fetched objects related to the one explicitly
asked for, it would also have to fetch the objects related to those,
and so on, until all of the interrelated rows in the database had
been retrieved. For many applications, this would be a waste of time
and resources. To avoid this, WebObjects creates empty destination objects,
called faults, that fetch their data the first time they're accessed.
This process, known as "faulting," is automatic.

**Uniquing**
: In marrying relational databases to object-oriented
programming, one of the key requirements is that a row in the database
be associated with only one enterprise object in a given context
in your application. WebObjects maintains the mapping of each enterprise
object to its corresponding database row, and uses this information
to ensure that, within a given context, your object set does not
include two (possibly inconsistent) objects for the same database
row. Uniquing of enterprise objects, as this process is called,
reduces memory usage and allows you to know with confidence that
the object you're interacting with represents the true state of
its associated row as it was last fetched.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Mapping_You_base_Tables.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](The_Enterpr_s_Advantage.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

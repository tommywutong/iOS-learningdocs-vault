---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.2d.html
archived_at: '2026-07-15T08:09:58.990124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Optimistic%20Locking.md) [!](Pessimistic%20Locking%20in%20Oracle.md)

#   Pessimistic Locking

##  Synopsis

Describes pessimistic locking.

##  Discussion

Although the default mechanism for locking in the Enterprise Objects Framework is optimistic locking, the framework also supports pessimistic locking. This type of locking works at the database level and prevents any other application or user from fetching or updating the same record at the same time. Pessimistic locking can be a very powerful mechanism, but often databases can impose limitations. Some databases, such as Oracle, lock a single record; others (for example, Sybase) lock a page or group of records; still others, including Microsoft Access, do not support pessimistic locking at all. You should check your database documentation to see how its pessimistic-locking system works, or if it has one at all. Also different database lock objects differently. Some databases, such as Oracle, prevent anyone else from fetching an object while others, such as Sybase, raise an exception when an attempt is made to update a record that has already been locked and updated.

EOF supports three different mechanisms or strategies for pessimistic locking: lock on select, lock on update, and lock on request.

###  Lock on Select

The locking on select mechanism locks objects when they are fetched. These objects remain locked until the first
saveChanges
or
revert
message affects them. After a
saveChanges
or
revert
, the locks are released; the objects are relocked only if they are refetched from the database. Use EODatabasesContext's
setUpdateStrategy
method to enable lock on select. The advantages of lock on select are the following:

- 

  It is easy to implement.
- 

  Lock on select, unlike the other two strategies for pessimistic locking, requires only one fetch to lock objects.

The disadvantages of lock on select are the following

- 

  It could lock more records than are necessary.
- 

  A fetch could raise an exception if the database is in a deadlock condition.

###  Lock on Update

The lock on update mechanism locks objects as soon as they are updated. When the object is first modified, EOF refetches the object for update. The objects remain locked until the first
saveChanges
or
revert
message is received. Implement locking on update by invoking EOEditingContext's
setLocksObjectsBeforeFirstModification
. The advantages of this mechanism are the following:

- 

  It is easy to implement.
- 

  It locks objects only when they are modified.
- 

  It reduces the number of locked objects.

The disadvantages of lock on update are the following:

- 

  Modifying an object could raise an exception if the database is in a deadlock condition.
- 

  An extra fetch is needed to lock the object.

###  Lock on Demand

You can choose to lock objects only when they are needed. This mechanism locks these objects until the first
saveChanges
or
revert
message is received. Implement lock on demand by invoking EOEditingContext's
lockObject
method. The advantages of lock on demand are the following:

- 

  You lock only the objects you need to lock.
- 

  Although this locking strategy could raise an exception if the lock causes a deadlock condition, it is easier to catch this exception than the exceptions potentially raised by either of the other two pessimistic locking strategies.

The disadvantages of lock on demand are the following:

- 

  It is more difficult to implement than the other mechanisms; you must decide when to lock objects.
- 

  An extra fetch is needed to lock the object.

##  See Also

- 

  [Choosing an Approach for Locking](Choosing%20an%20Approach%20for%20Locking.md#apple-ge2tmmjy)
- 

  [Optimistic Locking](Optimistic%20Locking.md#apple-ge4donrq)
- 

  [Locking on a Column](Locking%20on%20a%20Column.md#apple-geydinrx)
- 

  [Pessimistic Locking in Oracle](Pessimistic%20Locking%20in%20Oracle.md#apple-giztqnbs)
- 

  [Pessimistic Locking in Sybase](Pessimistic%20Locking%20in%20Sybase.md#apple-giydenrq)

##  Questions

- 

  What is pessimistic locking?
- 

  How can I prevent users from overwriting the work of others?
- 

  When can I lock objects pessimistically?

##  Keywords

- 

  Lock
- 

  Pessimistic

##  Revision History

22 July, 1998. Paul Haddad. First Draft.

18 November, 1998. Terry Donoghue. Second Draft.


```

```

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Optimistic%20Locking.md) [!](Pessimistic%20Locking%20in%20Oracle.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

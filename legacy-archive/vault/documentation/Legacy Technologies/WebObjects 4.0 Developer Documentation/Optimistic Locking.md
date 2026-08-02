---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/Optimistic_Locking.html
archived_at: '2026-07-15T08:01:18.985907Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Optimistic Locking

##  Synopsis

Describes optimistic locking.

##  Discussion

The default locking mechanism in the Enterprise Objects Framework is optimistic locking. Optimistic locking stores a snapshot of a database row as it is fetched. When EOF updates the record, it appends a qualifier to the update statement that ensures that the record will be updated only if none of the locking columns has been modified.

The only thing that you must do to support optimistic locking is to select an attribute's locking column in EOModeler. When the column is selected, a small lock icon appears in it. (This column is selected by default, so if you haven't unselected that column, you are using optimistic locking.)

As an example of optimistic locking in action, suppose you are updating the name of a Talent object from the Movies EOModel from "John Doe" to "Joe Doe". The Talent entity has optimistic locking enabled on all of its three columns (firstName, lastName, and talentID). When EOF updates the record, it creates a qualifier that ensures that none of those columns has been updated. The SQL statement looks something like the following:

```
update TALENT set FIRST_NAME = `Joe' where TALENT_ID = `123' and FIRST_NAME = `John' and LAST_NAME = `Doe';
```


By adding the first and last names prior to the change as part of the qualifier, this update only succeeds if no one else has modified this record. This mechanism ensures that two users will not overwrite one another's updates.

####  Lock on Some or All Columns?

You can specify optimistic locking on some or all columns of an entity. If you select locking on every column, all updates will fail if someone else has modified the record. However, if you know that a column will never be updated then there is no reason to lock on it. Either approach is easy and requires no additional database-table space. However, they both have disadvantages:

· Locking on all columns causes complex where clauses because EOF includes all previous values in the update's qualifier; these large where clauses could slow down your database. Locking on some columns, of course, mitigates this problem, but you can still have large where clauses.

· Some _BLOB_
data types (such as Oracle's RAW) may not be used as part of the qualifier. If you have an Oracle table with a primary key and a single _LONG RAW_
column, you cannot use this method of locking.

####   Using a Single Locking Column

If you want to trim the where clauses for updates, you can add a single class attribute whose value always changes during an update. Then set that attribute in EOModeler as the only one used for locking. When EOF updates the record, the only extra qualifier added is for this locking attribute. This approach has several advantages:

· It creates simpler and faster qualifiers. And by using this mechanism, you always know what the update qualifier looks like. With this information you can create a compound index between the locking attribute and the primary key of the table.

· This technique can be used with tables that have _BLOB_
columns.

· It requires no extra database-table space.

However, this technique is harder then standard optimistic locking. You must figure out a way to update the locking attribute when the object is changed (such as overriding the _willChange_
method or by catching the EOObjectsChangedInEditingContextNotification).

####  Using a Single Locking Column with Database Trigger

You can use a technique similar to the one described in "[See Using a Single Locking Column.](#apple-ge4tmnbr)
" but this time use a database-insert trigger to modify the locking attribute. (Note that triggers are specific to certain database.) You simply use an insert trigger to modify the locking attribute. The attribute should still be the only column that is selected for locking, but it should not be a class attribute.

As with the technique for using a single locking column, this one can be used with tables that have _BLOB_
columns and it requires no extra database-table space. It also creates simpler and faster qualifiers. This mechanism also allows you to know what the updates qualifier will look like and thus you can create a compound index between the locking column and the primary key of the table.

As with the technique described in "[See Using a Single Locking Column.](#apple-ge4tmnbr)
," you must figure out a way to update the locking column when the object is changed (such as overriding the _willChange_
method or by catching the _EOObjectsChangedInEditingContextNotification_
).

##  See Also

· Choosing an Approach for Locking

· Pessimistic Locking

· Locking on a Column

##  Questions

· What is optimistic locking?

· How can I prevent users from overwriting the work of others?

· Which columns should I lock on?

##  Keywords

· Locking

· Optimistic Locking

· Snapshot

##  Revision History

14 July, 1998. Paul Haddad. First Draft.

18 November, 1998. Terry Donoghue. Second Draft.

##### 

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

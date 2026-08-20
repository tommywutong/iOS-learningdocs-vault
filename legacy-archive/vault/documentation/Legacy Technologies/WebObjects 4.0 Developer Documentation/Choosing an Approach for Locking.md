---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/Choosing_an_Approach.html
archived_at: '2026-07-15T08:00:57.719618Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Choosing an Approach for Locking

##  Synopsis

Describes the different approaches for locking database records.

##  Discussion

"Locking" is a term that denotes a technique for preventing users from overwriting other users' work. There are four principal ways to implement locking: optimistic, pessimistic, locking on a column, and application-level locking. Each of these has different stengths and weaknesses and you are likely to use a combination of these approaches in your applications.

####  Optimistic Locking

Optimistic locking is the default locking mechanism for the Enterprise Objects Framework. With optimistic locking, database rows and objects are never actually locked. When an object is first read from the database, EOF makes a snapshot of that object. Before the data represented by the object is updated, the snapshot and database row are compared and if they are not the same, the update fails. The advantages of optimistic locking are the following:

· All databases support optimistic locking.

· Optimistic locking is easy to use.

· Optimistic locking doesn't use any extra database resources.

The disadvantages of optimistic locking are:

· Users are not notified that someone else modified a record until they try to update it.

· Optimistic locking slows down updates.

· All applications that update a database must agree on the columns to lock on.

####  Pessimistic Locking

Pessimistic locking locks database rows at the database level. Locking can happen either when the row is selected or on demand. Depending on the database, a select on a locked row either fails or is blocked until the row is unlocked. Some databases support support page-level locking. This means that whenever any row in a page is locked, a group of other rows is also locked. The advantages of pessimistic locking are:

· Pessimistic locking can prevent users and applications from reading data that is being changed.

· Users are notified immediately if they cannot access a database row.

· Pessimistic locking is easy to use.

The disadvantages of pessimistic locking are:

· Not all databases support this mechanism and the databases that do support it do so differently.

· Pessimistic locking uses extra database resources.

· Pessimistic locking can prevent other users from having read-only access to data.

· Pessimistic locking can cause deadlocks.

· Pessimistic locking can cause excessive locking.

####  Locking on a Column

One effective way to implement on-demand locking is to add a locked column to a database . An application can add a single column to a table and then change a value in the column to indicate whether an object is locked. This locked column can hold anything from a simple Boolean value to a user's name and a time stamp. The advantages of locking on a column are:

· This method lets the application decide when a record should be locked.

· This method enables users to see who locked the record and when it happened.

· You can give authorized users the capability to override the lock.

The disadvantages of locking on a column are:

· This method allows users to lock a record and keep it locked indefinitely.

· If the database connection is lost, the lock is still enabled.

· Extra database space is needed for the column.

· An extra transaction is needed to set the lock.

####  Application-level Locking

Locking at the application level is perhaps the most powerful locking mechanism, but it is the most difficult to implement. To lock at the application level, you must keep a list of locked objects shared by all applications that update the database. The advantages to application-level locking are the following:

· This technique allows much flexibility in the way an object is locked. Objects can be locked on demand, on read, on change, or on any combination of these.

· It enables the application to warn other users as soon as anyone locks an object.

· It requires no extra processing at the database level.

· No extra space is needed in the database.

The disadvantages of application-level locking are the following

· It can be very difficult and slow to keep a list of objects in synchronization with multiple applications running.

##  See Also

· Optimistic Locking

· Pessimistic Locking

· Locking on a Column

##  Questions

· What is locking?

· What are the different locking approaches?

· How can I prevent users from overwriting the work of others?

##  Keywords

· Locking

· Optimistic Locking

· Pessimistic Locking

· Forced Locking

· Application-level Locking

##  Revision History

10 July, 1998. Paul Haddad. First Draft.

18 November, 1998. Terry Donoghue. Second Draft.

##### 

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

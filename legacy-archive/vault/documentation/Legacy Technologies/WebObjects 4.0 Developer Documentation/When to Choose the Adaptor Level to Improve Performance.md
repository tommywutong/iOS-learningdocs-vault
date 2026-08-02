---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/ChoosingAdaptor.html
archived_at: '2026-07-15T08:00:56.686829Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# When to Choose the Adaptor Level to Improve Performance

##  Synopsis

Describes when and why you should program at the adaptor level.

##  Description

Enterprise Objects Framework (EOF) provides a set of high-level Application Programming Interfaces (APIs) for fetching databases directly into objects. This enables you to work at the object level and maintain consistency between the objects and the database. EOF high-level objects such as the EODisplayGroup or EOEditingContext hide the Structured Query Language (SQL) statements that insert, update, and delete rows in the database.

The adaptor level is a lower level of EOF that enables you to send raw SQL statements and request the database to execute stored procedures. The data from raw SQL fetches comes in the form of dictionaries which don't involve business objects. Therefore, using the adaptor level enables you to short-circuit all of the object management structure provided by EOF. Thus, you want to use the adaptor level when the overhead of using objects is too high, EOF cannot do what you want, or you don't really need the convenience of objects.

####  When to Use the Adaptor Level

When you insert, update, or delete a large number or rows, EOF must instantiate at least one object for each row. In addition, objects must be fetched from the database for updates and deletes. If a simple SQL statement can perform the operation, the adaptor level should be used because it minimizes network traffic and uses the database to instantiate rows and process queries, functions for which it has been optimized.

####  Tradeoffs with Using the Adaptor Level

The main issue you face when directly accessing the database is maintaining consistency between the objects in memory and the rows in the database. When you perform massive updates or deletes, your must refetch these objects, which can impact users. If only one instance of the application is running, you can invalidate the objects that might have been affected by the SQL statement. If there are several instances of the application, you might want to restart them or let them run with potentially inconsistent objects; both choices can confuse and hinder users.

####  When EOF Objects Cannot Do What You Need

When you may want to extract data that involves the grouping many rows, (computing the average or variance of the data, for example), you should send raw SQL and let the database engine do the work. You avoid the overhead of instantiating the objects and performing the computation. By sending raw SQL you can also count the number of rows you will fetch before you fetch them. If you are using optimized SQL requests or stored procedures shared by many applications, you obviously want to use the adaptor level to instruct the database to execute them.

##  See Also

· Updating with the Adaptor Level

· Inserting with the Adaptor Level

· Deleting with the Adaptor Level

· Executing Arbitrary SQL Statements

##  Questions

· How do I avoid instantiating and fetching many objects when I just need to do simple inserts/updates/deletes?

· How do I efficiently compute the average of a large number of database rows?

· Do I always need to instantiate objects to perform operations on the database?

· How do I efficiently compute the variance of a large number of database rows?

· How do I execute my own optimized SQL on a database?

##  Keywords

· Stored procedures

· Grouping

· SQL

· Performance

· Adaptor

##  Revision History

21 July, 1998. Jean-Luc Marsolier. First Draft of tradeoff section.

11 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

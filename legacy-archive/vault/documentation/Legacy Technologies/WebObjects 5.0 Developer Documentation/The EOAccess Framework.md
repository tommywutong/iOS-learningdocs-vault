---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Introduction.html
archived_at: '2026-07-15T08:13:41.925557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](EOAccessTOC.md)

# The EOAccess Framework

> **__Package:__**
> : com.webobjects.eoaccess

---

## Introduction

The EOAccess framework is one of a group of frameworks known collectively as the Enterprise Objects Framework. The classes and interfacesthat make up the EOAccess framework allow your applications to interact with database servers at a high level of abstraction. These classes make up what is known as the access layer. The access layer is divided into two main parts:

- The _database level_, which allows applications to treat records as full-fledged enterprise objects.
- The _adaptor level_, which provides server-independent database access.

Working with the access layer allows you to have a finer level of control over database operations.

## EOAccess Framework Class Hierarchy

The EOAccess class hierarchy is rooted in the Foundation Framework's NSObject class. The remainder of the EOAccess Framework consists of several related groups of classes, a few miscellaneous classes, and a number of interfaces.

## The Adaptor Level

The adaptor level deals with database rows packaged as dictionaries. The adaptor level is primarily made up of the following classes:

- EOAdaptor is an abstract class that provides concrete subclasses with a structure for connecting to a database.
- EOAdaptorChannel is an abstract class that provides its concrete subclasses with a structure for performing database operations.
- EOAdaptorContext is an abstract class that defines transaction handling in Enterprise Objects Framework applications.
- EOAdaptorOperation is a class that represents a primitive operation in a database server and all the necessary information required by the operation.
- EOLoginPanel is an abstract class that defines how users provide database login information.
- EOSQLExpression is an abstract superclass that defines how to build SQL statements for adaptor channels.

## The Database Level

The database level is where enterprise objects are created from the dictionaries retrieved by the adaptor level. It's also where snapshotting is performed. The database level is primarily made up of the following classes:

- EODatabase is a class that represents a single database server.
- EODatabaseChannel is a class that represents an independent communication channel to the database server.
- EODatabaseContext is subclass of EOObjectStore for accessing relational databases, creating and saving objects based on EOEntity definitions in an EOModel.
- EODatabaseOperation is a class that represents an operation-insert, update, or delete-to perform on an enterprise object and all the necessary information required to perform the operation.

## The Modeling Classes

A model defines, in entity-relationship terms, the mapping between enterprise object classes and a database. The following are the principal modeling classes in the EOAccess framework:

- EOAttribute is a class that represents a column, field or property in a database, and associates an internal name with an external name or expression by which the property is known to the database.
- EOEntity is a class that describes a table in a database and associates a name internal to the Framework with an external name by which the table is known to the database.
- EOJoin is a class that describes one source-destination attribute pair for an EORelationship.
- EOModel is a class that represents a mapping between a database schema and a set of classes based on the entity-relationship model.
- EOModelGroup is a class that represents an aggregation of related models.
- EORelationship is a class that describes an association between two entities, based on attributes of those two entities.
- EOStoredProcedure is a class that represents a stored procedure defined in a database, and associates a name internal to EOF with an external name known to the database.

## Faulting

These classes implement or are used to implement object faulting:

- EOAccessArrayFaultHandler is a subclass of EOAccessGenericFaultHandler that implements a fault for an array of enterprise objects.
- EOAccessFaultHandler is a subclass of EOAccessGenericFaultHandler that implements an object fault for enterprise objects.
- EOAccessGenericFaultHandler is an abstract class that helps an EOAccessFault to fire by fetching data using an EODatabaseContext.

## Extensions of EOControl Classes

The EOAccess framework also has a number of other useful classes, including:

- EODatabaseDataSource is a concrete subclass of EODataSource that fetches objects based on an EOModel, using an EODatabaseContext that services the data source's EOEditingContext.
- EOEntityClassDescription is a subclass of the control layer's EOClassDescription and extends the behavior of enterprise objects by deriving information about them from an associated EOModel.
- EOSQLQualifier is a subclass of EOQualifier that contains unstructured text that can be transformed into an SQL expression.

## Delegates

A number of EOAccess classes delegate behavior. The delegate methods are defined in these interfaces:

- An EOAdaptorChannel delegate receives messages for nearly every operation that would affect data in the database server, and it can preempt, modify, or track these operations.
- A EOAdaptorContext delegate receives messages for any transaction begin, commit, or rollback, and it can preempt, modify, or track these operations.
- An EOAdaptor delegate implements a method that can perform a database-specific transformations on a value.
- An EODatabaseContext delegate can intervene when objects are created and when they're fetched from the database.
- An EOModelGroup class delegate implements a method that returns the default model group.
- An EOModelGroup delegate influences how the model group finds and loads models.

## Miscellaneous Classes and Interfaces

- EOUtilities is a collection of convenience methods intended to make common operations with EOF easier.
- EOPropertyListEncoding declares methods that read and write objects to property lists.

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

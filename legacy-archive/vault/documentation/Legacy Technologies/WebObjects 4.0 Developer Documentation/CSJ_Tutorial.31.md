---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.31.html
archived_at: '2026-07-15T07:59:59.620459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.30.md) | [Table of Contents](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

##  Glossary

Several of the terms listed here apply to relational databases and entity-relationship modeling. Others apply strictly to Java Client applications.

####  adaptor

A mechanism that connects your application to a particular database server. For each type of server you use, you need a separate adaptor. Enterprise Objects Framework provides adaptors for Informix, Oracle, and Sybase servers, and for any server that is ODBC compliant.

####  attribute

In Entity-Relationship modeling, an identifiable characteristic of an entity. For example, __lastName__
can be an attribute of an __Employee__
entity. An attribute typically corresponds to a column in a database table. See _flattened attribute, entity,_
and _relationship_
.

####  class property

An instance variable in an enterprise object that meets two criteria: it's based on an attribute in your model, and it can be fetched from the database. "Class property" can either refer to an attribute or a relationship. In EOModeler you can specify class properties for server enterprise-object classes and class properties for client classes.

####  column

In a relational database, the dimension of a table that holds values for a particular attribute. For example, a table that contains employee records might have a column titled "LAST_NAME" that contains the values for each employee's last name. See _attribute_
.

####  compound primary key

In a database table, the group of columns whose values, taken in combination, are guaranteed to uniquely identify each row. See _primary_

_key_
.

####  data dictionary

In relational databases, the system tables that describe the organization of data in a particular database.

####  database server

A data storage and retrieval system. Database servers typically run on a dedicated computer and are accessed by client applications over a network.

####  enterprise object

An Objective-C or Java object that conforms to the key-value coding protocol, whose properties (instance data) can map to stored data. An enterprise object brings together stored data with the methods for operating on that data. See _key_
_-_
_value_

_coding_
and _property_
.

####  entity

In Entity-Relationship modeling, a distinguishable object about which data is kept. For example, you can have an Employee entity with attributes such as lastName, firstName, address, and so on. An entity typically corresponds to a table in a relational database; an entity's attributes in turn correspond to a table's columns. See _attribute_
and _table_
.

####  Entity-Relationship modeling

A discipline for examining and representing the components and interrelationships in a database system. Also known as E-R modeling, this discipline factors a database system into entities, attributes, and relationships.

####  fetch

In Enterprise Objects Framework applications, to retrieve data from the database server into the client application, usually into enterprise objects.

####  flattened attribute

A special kind of attribute that you add from one entity to another by traversing a relationship. For example, employees work for departments; you can add an attribute (such as departmentName) from the Department entity to the Employee entity as a flattened attribute. A flattened attribute is normally implemented by joining the tables corresponding to the source and destination entities whenever the attribute's data is fetched. See _relationship_
and
_attribute_
.

####  foreign key

An attribute in an entity that gives it access to rows in another entity. This attribute must be the primary key of the related entity. For example, an Employee entity can contain the foreign key deptID, which matches the primary key in the entity Department. You can then use deptID as the source attribute in Employee and as the destination attribute in Department to form a relationship between the entities. See _key, primary key,_
and _relationship_
.

####  generic record

An instance of the EOGenericRecord default enterprise object class. A generic record has properties that map to stored data, but unlike a custom enterprise object, it adds no behavior to that data. Like custom enterprise objects, generic records conform to the key-value coding protocol; see _key_
_-_
_value_

_coding_
.

####  interface controller

An instance of a subclass of EOInterfaceController that is the owner of a nib file containing a "Java archive" describing a user interface made up of "Swing" (Java Foundation Classes) objects.

####  join

An operation that provides access to data from two tables at the same time, based on the values contained in related columns.

####  key-value coding

The mechanism that allows the properties in enterprise objects to be accessed by name (that is, as key-value pairs) by other parts of the Framework.

####  many-to-many relationship

A relationship in which each record in the source entity may correspond to more than one record in the destination entity, and each record in the destination may correspond to more than one record in the source. For example, an employee can work on many projects, and a project can be staffed by many employees. See _relationship_
.

####  model

An EOModel object that defines, in Entity-Relationship terms, the mapping between enterprise object classes and the database schema. This definition is typically stored in a file created with the EOModeler application. A model also includes the information needed to connect to a particular database server; see _connection_

_dictionary_
.

####  record

The set of values that describes a single instance of an entity; in a relational database, a record is equivalent to a row.

####  relational database

A database designed according to the relational model, which uses the discipline of Entity-Relationship modeling and the data design standards called normal forms.

####  relationship

A link between two entities that's based on attributes of the entities. For example, the Department and Employee entities can have a relationship based on the deptID attribute as a foreign key in Employee, and as the primary key in Department (note that though the join attribute deptID is the same for the source and destination entities in this example, it doesn't have to be). This relationship would make it possible to find the employees for a given department. See _t_
_o-one, to-many, many-to-many, primary key,_
and _foreign key_
.

####  row

In a relational database, the dimension of a table that groups attributes into records.

####  table

A two-dimensional set of values corresponding to an entity. The columns of a table represent characteristics of the entity and the rows represent instances of the entity.

####  to-many relationship

A relationship in which each source record has zero to many corresponding destination records. For example, a department has many employees

####  to-one relationship

A relationship in which each source record has exactly one corresponding destination record. For example, each employee has one job title.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.30.md) | [Table of Contents](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

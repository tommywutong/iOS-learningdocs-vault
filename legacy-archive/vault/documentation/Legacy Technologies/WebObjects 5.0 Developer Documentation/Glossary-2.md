---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/Glossary/Glossary.html
archived_at: '2026-07-15T08:13:19.753370Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/iSorting_a_Fetch.html)

# Glossary

**__adaptor, database__**
: A
mechanism that connects your application to a particular database
server. For each type of server you use, you need a separate adaptor.
WebObjects provides an adaptor for databases conforming to JDBC.

**__adaptor, WebObjects__**
: A process (or a part of one) that connects
WebObjects applications to an HTTP server.

**__application object__**
: An object (of the WOApplication class) that
represents a single instance of a WebObjects application. The application
object's main role is to coordinate the handling of HTTP requests,
but it can also maintain application-wide state information.

**__attribute__**
: In Entity-Relationship modeling, an identifiable
characteristic of an entity. For example, `lastName` can
be an attribute of an Employee entity. An attribute typically corresponds
to a column in a database table. See also __entity__; __relationship__.

**__business logic__**
: The rules associated with the data in a database
that typically encode business policies. An example is automatically
adding late fees for overdue items.

**__CGI__**
: A standard for communication between external
applications and information servers, such as HTTP or Web servers.
Short for Common Gateway Interface.

**__class__**
: In object-oriented languages such as Java, a
prototype for a particular kind of object. A class definition declares
instance variables and defines methods for all members of the class. Objects
that have the same types of instance variables and have access to
the same methods belong to the same class.

**__class property__**
: An instance variable in an enterprise object
that meets two criteria: it's based on an attribute in your model,
and it can be fetched from the database. A class property can be
an attribute, a relationship, a method, or an instance variable.

**__column__**
: In a relational database, the dimension of
a table that holds values for a particular attribute. For example,
a table that contains employee records might have a LAST_NAME column
that contains the values for each employee's last name. See also __attribute__.

**__component__**
: An object (of the WOComponent class) that represents
a Web page or a reusable portion of one.

**__context__**
: An object that encapsulates state information
for a given transaction (one cycle of the request-response loop).
Context objects are implemented with the WOContext class. They encapsulate
information about the URL, context ID, application, session, component,
request, and response items. WebObjects maintains a cache of WOContext
objects to support the back function of Web browsers. See also __request-response
loop__.

**__cookie__**
: General mechanism used by Web servers to store
and retrieve persistent data on a client system (Web browser). The
information stored is usually state data associated with a range
of URLs.

**__database server__**
: A data storage and retrieval system. Database
servers typically run on a dedicated computer and are accessed by
client applications over a network.

**__delete rule__**
: A delete rule specifies the action to take
when the source object of a relationship is deleted from the data
store. The possible actions are nullify, cascade, deny, and none.
Delete rules are defined in model files with the EOModeler application.
See also __relationship__.

**__display group__**
: A display group collects an array of objects
from a data source, sorts it and displays data from the objects
in the user interface. See also __EODisplayGroup__; __WODisplayGroup__.

**__dynamic element__**
: A dynamic version of an HTML element. WebObjects
includes a list of dynamic elements with which you can build your
component.

**__enterprise object__**
: A Java object that conforms to the key-value
coding protocol and whose properties (instance data) can map to
stored data. An enterprise object brings together stored data with
methods for operating on that data. See also __key-value
coding__; __property__.

**__entity__**
: In Entity-Relationship modeling, a distinguishable
object about which data is kept. For example, you can have an Employee
entity with attributes such as `lastName`, `firstName`, `address`,
and so on. An entity typically corresponds to a table in a relational
database; an entity's attributes, in turn, correspond to a table's
columns. See also __attribute__; __table__.

**__Entity-Relationship modeling__**
: A Discipline for examining and representing
the components and interrelationships in a database system. Also known
as E-R modeling, this discipline factors a database system into
entities, attributes, and relationships.

**__EODisplayGroup__**
: A display group that displays data in J2SE
or Cocoa interface elements using EOAssociations. See also __display
group__.

**__EOModeler__**
: A tool used to create and edit models.

**__fetch__**
: In Enterprise Objects applications, to retrieve
data from the database server into the client application, usually
into enterprise objects.

**__foreign key__**
: An attribute in an entity that gives it access
to rows in another entity. This attribute must be the primary key
of the related entity. For example, an Employee entity can contain
the foreign key `deptID`,
which matches the primary key in the entity Department. You can
then use `deptID` as the
source attribute in Employee and as the destination attribute in
Department to form a relationship between the entities. See also __primary
key__; __relationship__.

**__HTML-based application
approach__**
: A WebObjects development
approach that allows you to create HTML-based Web applications.

**__inheritance__**
: In object-oriented programming, the ability
of a superclass to pass its characteristics (methods and instance
variables) on to its subclasses.

**__instance__**
: In object-oriented languages such as Java,
an object that belongs to (is a member of) a particular class. Instances
are created at runtime according to the specification in the class definition.

**__Java Browser__**
: A tool used to peruse Java APIs and class hierarchies.

**__Java Foundation Classes__**
: A set of graphical user interface components
and services written in Java. The component set is known as Swing.

**__JDBC__**
: Stands for "Java Database Connectivity."
An interface between Java platforms and databases.

**__key__**
: An arbitrary value (usually a string) used to
locate a datum in a data structure such as a dictionary.

**__key-value coding__**
: The mechanism that allows the properties in
enterprise objects to be accessed by name (that is, as key-value
pairs) by other parts of the application.

**__key-value pair__**
: See __key-value coding__.

**__locking__**
: A mechanism to ensure that data isn't modified
by more than one user at a time and that data isn't read as it
is being modified.

**__many-to-many relationship__**
: A relationship in which each record in the
source entity may correspond to more than one record in the destination
entity, and each record in the destination may correspond to more
than one record in the source. For example, an employee can work
on many projects, and a project can be staffed by many employees.
See also __relationship__.

**__method__**
: In object-oriented programming, a procedure
that can be executed by an object.

**__model__**
: An object (of the EOModel class) that defines,
in Entity-Relationship terms, the mapping between enterprise object
classes and the database schema. This definition is typically stored
in a file created with the EOModeler application. A model also includes
the information needed to connect to a particular database server.

**__object__**
: A programming unit that groups together a data
structure (instance variables) and the operations (methods) that
can use or affect that data. Objects are the principal building blocks
of object-oriented programs.

**__primary key__**
: An attribute in an entity that uniquely identifies
rows of that entity. For example, the Employee entity can contain
an `EmpID` attribute that
uniquely identifies each employee.

**__Project Builder__**
: A tool used to manage the development of a
WebObjects application or framework.

**__property__**
: In Entity-Relationship modeling, an attribute
or relationship. See also __attribute__; __relationship__.

**__record__**
: The set of values that describes a single instance
of an entity; in a relational database, a record is equivalent to
a row.

**__relational database__**
: A database designed according to the relational
model, which uses the discipline of Entity-Relationship modeling
and the data design standards called normal forms.

**__relationship__**
: A link between two entities that's based
on attributes of the entities. For example, the Department and Employee
entities can have a relationship based on the `deptID` attribute
as a foreign key in Employee and as the primary key in Department
(note that although the join attribute `deptID` is
the same for the source and destination entities in this example,
it doesn't have to be). This relationship would make it possible
to find the employees for a given department. See also __foreign
key__: __many-to-many relationship__; __primary
key__; __to-many relationship__; __to-one
relationship__.

**__reusable component__**
: A component that can be nested within other
components and acts like a dynamic element. Reusable components
allow you to extend the WebObject's selection of dynamically generated
HTML elements.

**__request__**
: A message conforming to the Hypertext Transfer
Protocol (HTTP) sent from the user's Web browser to a Web server
that asks for a resource like a Web page. See also __response__.

**__request-response loop__**
: The main loop of a WebObjects application that
receives a request, responds to it, and awaits the next request.

**__response__**
: A message conforming to the Hypertext Transfer
Protocol (HTTP) sent from the Web server to the user's Web browser
that contains the resource specified by the corresponding request.
The response is typically a Web page. See also __request__.

**__row__**
: In a relational database, the dimension of a
table that groups attributes into records.

**__rule__**
: In the Direct to Web and Direct to Java Client
approaches, a specification used to customize the user interfaces
of applications developed with these approaches.

**__session__**
: A period during which access to a WebObjects
application and its resources is granted to a particular client
(typically a browser). Also an object (of the WOSession class) representing
a session.

**__target__**
: A blueprint for building a product from specified
files in your project. It consists of a list of the necessary files
and specifications on how to build them. Some common types of targets build
frameworks, libraries, applications, and command-line tools

**__table__**
: A two-dimensional set of values corresponding
to an entity. The columns of a table represent characteristics of
the entity and the rows represent instances of the entity.

**__template__**
: In a WebObjects component, a file containing
HTML that specifies the overall appearance of a Web page generated
from the component.

**__to-many relationship__**
: A relationship in which each source record
has zero to many corresponding destination records. For example, a
department has many employees.

**__to-one relationship__**
: A relationship in which each source record
has exactly one corresponding destination record. For example, each
employee has one job title.

**__transaction__**
: A set of actions that is treated as a single
operation.

**__uniquing__**
: A mechanism to ensure that, within a given
context, only one object is associated with each row in the database.

**__validation__**
: A mechanism to ensure that user-entered data
lies within specified limits.

**__Web server__**
: An application that serves Web pages to Web
browsers using the HTTP protocol. In WebObjects, the Web server
lies between the browser and a WebObjects application. When the
Web server receives a request from a browser, it passes the request
to the WebObjects adaptor, which generates a response and returns it
to the Web server. The Web server then sends the response to the
browser. See also adaptor, WebOBjects; __request-response
loop__.

**__WebObjects Builder__**
: A tool used to graphically edit WebObjects
components.

**__WODisplayGroup__**
: A display group that displays data in WebObjects
components. See also __display group__.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFRelationships/iSorting_a_Fetch.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

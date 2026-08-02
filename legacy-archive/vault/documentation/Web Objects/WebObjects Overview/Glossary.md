---
title: WebObjects Overview
apple_id: TP30001008
resource_type: Guide
platform: macOS
topic: null
technology: WebObjects
published: '2007-07-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/WebObjects_Overview/Glossary/Glossary.html
archived_at: '2026-07-18T02:21:58.690513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Overview](Introduction%20to%20WebObjects%20Overview.md)


[Next](Index.md)[Previous](Document%20Revision%20History.md)

# Glossary

- __business logic__

  The rules associated with the data in a database that typically encode business policies. An example is automatically adding late fees for overdue items.

- __CGI (Common Gateway Interface)__

  A standard for interfacing external applications with information servers, such as HTTP or web servers.

- __class__

  In object-oriented languages such as Java, a prototype for a particular kind of object. A class definition declares instance variables and defines methods for all members of the class. Objects that have the same types of instance variables and have access to the same methods belong to the same class.

- __column__

  In a relational database, the dimension of a table that holds values for a particular attribute. For example, a table that contains employee records might have a LAST_NAME column that contains the values for each employee’s last name.

- __database server__

  A data storage and retrieval system. Database servers typically run on a dedicated computer and are accessed by client applications over a network.

- __Direct to Java Client__

  A WebObjects development approach that can generate a Java Client application from a model.

- __Direct to Java Client Assistant__

  A tool used to customize a Direct to Java Client application.

- __Direct to Web__

  A WebObjects development approach that can generate a web application from a model.

- __Direct to Web Services__

  A WebObjects development approach that can generate a web service application from a model.

- __Direct to Web template__

  A component used in Direct to Web applications that can generate a webpage for a particular task (for example, a list page) for any entity.

- __dynamic element__

  A dynamic version of an HTML element. WebObjects includes a list of dynamic elements with which you can build web components.

- __enterprise object__

  An object that conforms to the key-value coding protocol and whose properties can map to stored data. An enterprise object brings together stored data with methods for operating on that data.

- __Enterprise Objects__

  Enterprise Objects is a set of frameworks to build feature-rich database applications that encapsulate your business logic, yet are independent of any particular data source.

- __entity__

  In Entity-Relationship modeling, a distinguishable object about which data is kept. For example, you can have an Employee entity with attributes such as `lastName`, `firstName`, `address`, and so on. An entity typically corresponds to a table in a relational database; an entity’s attributes, in turn, correspond to a table’s columns.

- __Entity-Relationship modeling__

  A discipline for examining and representing the components and interrelationships in a database system. Also known as ER modeling, this discipline factors a database system into entities, attributes, and relationships.

- __EOModeler__

  A tool used to create and edit models.

- __faulting__

  A mechanism used by WebObjects to increase performance whereby destination objects of relationships are not fetched until they are explicitly accessed.

- __fetch__

  In Enterprise Objects applications, to retrieve data from the database server into the client application, usually into enterprise objects.

- __HTTP adaptor__

  A process (or a part of one) that connects WebObjects applications to a web server.

- __instance__

  In object-oriented languages such as Java, an object that belongs to (is a member of) a particular class. Instances are created at runtime according to the specification in the class definition.

- __Interface Builder__

  A tool used to create and edit graphical user interfaces like those used in Java Client applications.

- __Java Client__

  A WebObjects development approach that allows you to create graphical user interface applications that run on the user’s computer and communicate with a WebObjects server.

- __JFC (Java Foundation Classes)__

  A set of classes that implement graphical user interface components, also called Swing components.

- __JDBC__

  An interface between Java platforms and databases.

- __key__

  An arbitrary value (usually a string) used to locate a datum in a data structure such as a dictionary.

- __method__

  In object-oriented programming, a procedure that can be executed by an object.

- __model__

  An object (of the EOModel class) that defines, in Entity-Relationship terms, the mapping between enterprise object classes and the database schema. This definition is typically stored in a file created with the EOModeler application. A model also includes the information needed to connect to a particular database server.

- __Model-View-Controller__

  An object-oriented programming paradigm in which the functions of an application are separated into the special knowledge (model objects), user interface elements (view objects), and the interface that connects them (the controller object).

- __object__

  A programming unit that groups together a data structure (instance variables) and the operations (methods) that can use or affect that data. Objects are the principal building blocks of object-oriented programs.

- __record__

  The set of values that describes a single instance of an entity; in a relational database, a record is equivalent to a row.

- __relational database__

  A database designed according to the relational model, which uses the discipline of Entity-Relationship modeling and the data design standards called normal forms.

- __relationship__

  A link between two entities that’s based on attributes of the entities. For example, the Department and Employee entities can have a relationship based on the `deptID` attribute as a foreign key in Employee, and as the primary key in Department. This relationship would make it possible to find the employees for a given department.

- __reusable component__

  A component that can be nested within other components and acts like a dynamic element.

- __request__

  A message conforming to the Hypertext Transfer Protocol (HTTP) sent from the user’s web browser to a web server that asks for a resource like a webpage.

- __response__

  A message conforming to the Hypertext Transfer Protocol (HTTP) sent from the web server to the user’s web browser that contains the resource specified by the corresponding request. The response is typically a webpage.

- __row__

  In a relational database, the dimension of a table that groups attributes into records.

- __session__

  A period during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). Also an object (of the WOSession class) representing a session.

- __table__

  A two-dimensional set of values corresponding to an entity. The columns of a table represent characteristics of the entity and the rows represent instances of the entity.

- __to-many relationship__

  A relationship in which each source record has zero to many corresponding destination records. For example, a department has many employees.

- __to-one relationship__

  A relationship in which each source record has exactly one corresponding destination record. For example, each employee has one job title.

- __transaction__

  A set of actions that is treated as a single operation.

- __Web Assistant__

  Tool used to customize a Direct to Web application.

- __Web component__

  An object (of the WOComponent class) that represents a webpage or a reusable portion of one.

- __Webpage template__

  HTML file that specifies the overall appearance of a webpage generated from a web component.

- __Web Services Assistant__

  Application used to customize a Direct to Web Services applications.

- __WebObjects Builder__

  An application used to edit web components.

[Next](Index.md)[Previous](Document%20Revision%20History.md)


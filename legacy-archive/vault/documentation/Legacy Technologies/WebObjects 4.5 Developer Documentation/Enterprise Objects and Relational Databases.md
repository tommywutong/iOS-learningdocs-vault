---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.e.html
archived_at: '2026-07-15T08:09:18.381983Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](Requirements.md) [!](What%20Goes%20Into%20the%20StudioManager%20Application.md)

---

#  Enterprise Objects and Relational Databases

The Studio, Movie, and Talent enterprise object classes correspond to tables in a relational database. For example, the Studio enterprise object corresponds to the STUDIO table in the database, which has NAME and BUDGET columns. The Studio enterprise object class in turn has __name__ and __budget__ instance variables, or class properties (instance variables based on database data are called "class properties"). In an application, Studio objects are instantiated using the data from a corresponding database row, as shown in the following figure:

!

The enterprise objects in your application do not merely form a static representation of your database data, however. Enterprise objects add behavior to your data. For example, the Studio enterprise object class has a method for calculating the studio's portfolio value based on the revenue of its movies. It also has a method for buying all of the movies starring a specified actor.

In Java Client WebObjects applications, Enterprise 

Objects Framework manages the interaction between the database (on the server), your enterprise objects (on the server and client), and the user interface (on the client). Its primary responsibilities are as follows:

- 

  Fetching data from relational databases into enterprise objects (on the server)
- 

  Binding data in enterprise objects to the user interface (on the client)
- 

  Keeping objects in the application synchronized with each other, with the database, and with the user interface; this includes keeping enterprise objects on the client synchronized with their counterparts on the server.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](Requirements.md) [!](What%20Goes%20Into%20the%20StudioManager%20Application.md)

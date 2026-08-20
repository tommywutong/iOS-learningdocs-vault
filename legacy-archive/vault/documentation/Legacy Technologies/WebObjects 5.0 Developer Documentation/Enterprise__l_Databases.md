---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/Enterprise__l_Databases.html
archived_at: '2026-07-15T08:14:17.674461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](The_Studio__Application.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Goes_I_Application.md)

## Enterprise Objects and Relational Databases

The Studio, Movie, and Talent enterprise object classes correspond
to tables in a relational database (WOMovies). For example, the
Studio enterprise object corresponds to the STUDIO table in the
database, which has NAME and BUDGET columns. The Studio enterprise
object class in turn has `name` and `budget` instance
variables, or class properties (instance variables based on database
data are called "class properties"). In the application, Studio
objects are instantiated using the data from a corresponding database
row, as shown in the following figure:

![[image: ../Art/eo.gif]](../Art/eo.gif)

The enterprise objects in your application do not merely form
a static representation of your database data, however. Enterprise
objects add behavior to your data. For example, the Studio enterprise
object class has a method for calculating the studio's portfolio
value based on the revenue of its movies. It also has a method for
buying all of the movies starring a specified actor.

In Java Client WebObjects applications, Enterprise Objects
Framework manages the interaction between the database (on the server),
your enterprise objects (on the server and client), and the user
interface (on the client). Its primary responsibilities are as follows:

- fetching
  data from relational databases into enterprise objects (on the server)
- binding data in enterprise objects to the user interface (on
  the client)
- keeping objects in the application synchronized with each
  other, with the database, and with the user interface; this includes
  keeping enterprise objects on the client synchronized with their
  counterparts on the server

[![Previous](attachments/JavaClient/Images/previous.gif)](The_Studio__Application.md)[![Next](attachments/JavaClient/Images/next.gif)](What_Goes_I_Application.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

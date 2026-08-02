---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.9.html
archived_at: '2026-07-15T08:00:05.389728Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.8.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.a.md)

##  Enterprise Objects and  Relational Databases

The Studio, Movie, and Talent enterprise object classes correspond to tables in a relational database. For example, the Studio enterprise object corresponds to the STUDIO table in the database, which has NAME and BUDGET columns. The Studio enterprise object class in turn has __name__
and __budget__
instance variables, or _class properties_ (instance variables based on database data are called "class properties"). In an application, Studio objects are instantiated using the data from a corresponding database row, as shown in the following figure:

###### 

!

The enterprise objects in your application do not merely form a static representation of your database data, however. Enterprise objects add behavior to your data. For example, the Studio enterprise object class has a method for calculating the studio's portfolio value based on the revenue of its movies. It also has a method for buying all of the movies starring a specified actor.

In Java Client WebObjects applications, Enterprise 

Objects Framework manages the interaction between the database (on the server), your enterprise objects (on the server and client), and the user interface (on the client). Its primary responsibilities are as follows:

- Fetching data from relational databases into enterprise objects (on the server)

- Binding data in enterprise objects to the user interface (on the client)

- Keeping objects in the application synchronized with each other, with the database, and with the user interface; this includes keeping enterprise objects on the client synchronized with their counterparts on the server.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.8.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.a.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

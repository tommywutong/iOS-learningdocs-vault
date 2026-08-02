---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2.html
archived_at: '2026-07-15T07:59:40.539321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.3.md)

##  Java Client Architecture

A Java Client application is essentially an Enterprise Objects Framework application distributed across an application server (running a WebObjects application) and one or more Web-browser clients (running applets). As a starting point, consider the following diagram, which depicts a "traditional" desktop Enprise Objects Framework application.

###### 

!

#####       Architecture of Traditional Enterprise Objects Framework Application

In this architecture data is fetched from databases through the EOAdaptor layer, objects of which (adaptors) interact with specific database servers. The EOAccess layer creates enterprise objects from the "raw" fetched data and registers these with the EOControl layer; the access layer, through EOModel and related classes, also provides a mapping between the database schema and enterprise objects. The EOControl layer manages a graph of enterprise objects, tracks changes to them, and directs the access layer to commit changes to those objects. Finally, the EOInterface layer in this traditional desktop application synchronizes the data displayed in the user interface--here objects of the Application Kit framework--with the EOControl layer's graph of enterprise objects.

The design of Java Client breaks up some of these layers and redistributes them across the client and the application server, which occupies the middle tier in the overall architecture. The following figure illustrates how this is done.

######  

!
> #####       Architecture of Java Client

Java Client moves the pieces that perform object-to-UI-mapping to the client and duplicates the control layer on the client so that the graph of enterprise objects and the management of that graph occurs on both server and client. It also adds a new layer to both client and server, the EODistribution layer, which performs by-copy object distribution and synchronization. The final difference, of course, is the use of the Java Foundation Classes as the user-interface framework. (The object-to-database mapping layer, EOAccess, remains solely on the server.)

The diagram in [Figure 2](#apple-gi4dsobr)
seems to suggest a lot of complexity, but it is important to keep in mind that the functionality it implies (and the amount of code required to implement it) are inherent in all true multi-tier architectures. Java Client provides most of the code for you. Unlike other multi-tier approaches, you do not have to worry about such things as change tracking, data packaging, and UI synchronization. In most cases, you need only write your business-logic code.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.1.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

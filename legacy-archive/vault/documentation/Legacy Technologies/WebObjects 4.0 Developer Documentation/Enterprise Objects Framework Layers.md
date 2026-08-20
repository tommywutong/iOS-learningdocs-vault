---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/WhatsEOF6.html
archived_at: '2026-07-18T01:19:53.535318Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](Ingredients%20of%20an%20Enterprise%20Objects%20Framework%20Application.md)

# Enterprise Objects Framework Layers

Conceptually, Enterprise Objects Framework is divided into four layers: the access layer, the control layer, the interface layer, and the distribution layer. Correspondingly, it partitions its classes and interfaces into four frameworks: EOAccess, EOControl, EOInterface, and EODistribution. The names of the layers and frameworks are used interchangeably throughout the Framework documentation.
This section introduces the Framework layers by demonstrating the roles they play in the four most basic types of Enterprise Objects Framework applications.

## A Command-Line Program

The simplest type of application is a command-line program (any program that doesn't have a graphical user interface). As shown in [Figure 7](#apple-haydioi), a command line program uses only the most fundamental layers of the Framework: the access layer and the control layer.

!

Figure 7. A Command-Line Program

Using a model, the _access layer_ fetches rows of data from a database, creates enterprise objects from the fetched data, and registers the enterprise objects with the control layer. The _control layer_ manages the graph of enterprise objects in memory, tracking changes to them and directing the access layer to commit those changes to the database when the program is ready to save.

## An Application Kit Client/Server Application

The second type of application is a traditional client/server application in which desktop clients access a database running on a server. To the simple architecture of a command-line program, a desktop client adds a graphical user interface and two additional frameworks to support that interface ([Figure 8](#apple-gqzdomq)).

!

Figure 8. An Application Kit Client/Server Application

The _Application Kit_ is a framework that provides the structure and
user-interface controls (buttons, text fields, and tables, for example) for applications with graphical user interfaces. The Application Kit isn't a part of Enterprise Objects Framework; rather it's a fundamental component of the Yellow Box development environment. For more information on the Application Kit, see the "Introduction to the Application Kit" in the _Application Kit Reference_.
On the other hand, _interface layer_ is a part of Enterprise Objects Framework. It maps data between the application's user interface and the control layer's graph of enterprise objects.

## An HTML WebObjects Application

The third type of application is an HTML web application. Like the Application Kit client/server application, the HTML web application uses the access and control layers to fetch and manage enterprise objects. However, the HTML web application replaces the Application Kit-based user interface with a standard, HTML web page ([Figure 9](#apple-gmydcma)).

!

Figure 9. An HTML WebObjects Application

The _WebObjects_ framework manages the user interface in an HTML web application. It combines the functionality of the Application Kit and EOInterface to provide an HTML-based presentation layer. Like the Application Kit, the WebObjects framework provides structure and
user-interface elements. It also provides its own mechanism for transporting data between the control layer's graph of enterprise objects and a web page. WebObjects framework, like the Application Kit, is not a part of Enterprise Objects Framework. Rather, it's the fundamental component of the WebObjects product. For more information on the WebObjects framework, see the _WebObjects Developer's Guide_.
The Application Kit client/server application and the HTML web application are both client/server applications; but in the former, the client is fat, and in the latter, the client is thin. Put another way, the Application Kit application puts all (or most) of the application and business logic in the client, whereas the HTML web application puts all (or most) of the application and business logic in the application server.
In contrast, a web application with Java client distributes the logic more evenly across the client and the application server (Figure 4). This last type of application introduces the final Enterprise Objects Framework layer: the _distribution layer_ keeps copies of enterprise objects in the application server synchronized with those in the client.

!

Figure 10. A Web Application with a Java Client

The kinds of applications you can build with Enterprise Objects Framework aren't limited to these four types; the types in this chapter are simply the most basic. They can be mixed and matched to create numerous other configurations. For example, you could build a command-line application to act as a server for an Application Kit-based desktop client, distributing your business logic across the client and server the way you can with a web application and a Java client.

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/WhatsEOF5.html
archived_at: '2026-07-15T08:03:24.926516Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Previous Section](From%20Objects%20to%20Database.md)

# Ingredients of an Enterprise Objects Framework Application

Enterprise Objects Framework can be used to create many different kinds of applications:

- Command-line programs without a graphical user interface
- Application Kit client/server desktop applications where all the logic is in a client
- HTML WebObjects applications where all the logic is in the application server
- WebObjects applications with interactive Java clients where the logic is distributed between an application server and its clients

Regardless of the type of application you're building (and assuming your data store is a relational database), creating an Enterprise Objects Framework application usually involves the following components (shown in [Figure 6](#apple-geydemrv)).

- _A user interface._ The type of interface you want-whether a graphical user interface based on Apple's Application Kit for a desktop application, an HTML web interface based on Apple's WebObjects framework, or an interactive Java client (using Sun's JDK user interface objects) for a web application-determines the tools you use to create the user interface. For Application Kit applications and Java web clients, you use Interface Builder. For HTML web applications, you use WebObjects Builder.
- _A model._ A model defines the mapping between your enterprise objects and the data stored in your database. An enterprise object class typically corresponds to a table in a database, and an enterprise object instance corresponds to a single row or record in the corresponding table. You define and store this correspondence in models that you build graphically with the EOModeler application.
- _Enterprise Objects._ These are your business objects, in custom code that you provide. Enterprise objects couple data from the database with the business logic required to operate on that data.
- _Enterprise Objects Framework's classes and interfaces._ The classes and interfaces (or classes and _protocols_ if you're using Objective-C) let you programmatically manipulate data as it passes between the database server, your enterprise objects, and the user interface. Although simple applications can be created entirely in one of the builder tools, sophisticated applications require using some of the Enterprise Objects Framework classes in your own code.
- _A database server and an adaptor for that server._ An adaptor is a mechanism that connects your application to a particular server. For each type of server you use, you need a separate adaptor. Enterprise Objects Framework provides adaptors for Oracle, Sybase, Informix, and ODBC-compliant servers. It also provides a sample adaptor for a flat-file data store and an adaptor for OpenBase Lite-a database that ships with Enterprise Objects Framework as an unsupported demo.

What varies between different types of applications is the parts of the Framework that you use and how they interact with your application's user interface.

!

Figure 6. The Ingredients of an Enterprise Objects Framework Application

[!Table of Contents](What%20Is%20Enterprise%20Objects%20Framework.md) [!Next Section](Enterprise%20Objects%20Framework%20Layers.md)

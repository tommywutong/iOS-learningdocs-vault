---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/JavaClient/Development_s_and_Tools.html
archived_at: '2026-07-15T08:15:09.786610Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Other_Architectures.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Advantages__nt_Approach.md)

## Development Tasks and Tools

The most basic tasks of creating a Java Client application
are as follows:

- Create a
  project using Project Builder.
- Create a model using EOModeler.
- Write source code for enterprise object classes.
- Create your application's user interface with Interface
  Builder.
- Write source code for any application-level logic.

The tasks have much in common with those for developing HTML-based
WebObjects applications. The major differences are the way you design
your enterprise object classes and the way you create your application's
user interface.

### Designing Enterprise Objects for Java Client

Java Client allows you to specify two enterprise object classes
for each entity: one for the server and one for the client. The
client and server classes can have different sets of properties
and business logic. This means that programming a Java Client WebObjects application
requires a specific design technique that isn't necessary in HTML-based development:
object partitioning. Simply put, you have to determine whether you
need different enterprise object classes for the client and the
server and also what data and business logic to put in each class.

Usually, client objects have the more restricted set of data
and behaviors, but it is really up to you to decide based on the
requirements of the application and your business. As noted earlier,
the primary criteria for partitioning are performance and security.

### Creating the User Interface

A Java Client WebObjects application gives you considerable
flexibility in how you compose its user interface. Ideally you provide
an application's entire user interface in a single Java application
that runs on the client. But you can also combine Java Client applets and
static and dynamic (WebObjects) HTML elements in various ways. You
can have pages with or without Java Client applets or pages with
multiple Java Client applets. For example, you could have a login
page that takes the user to one of many Java Client pages based
on some piece of account data. In addition, Java Client applets
are not limited to the downloaded JFC components; as with any applet,
they can create dialogs and secondary windows on the fly.

If your application's user interface uses static and dynamically
generated HTML, you create those parts of the user interface in
the normal way with WebObjects Builder (as described in ["HTML-Based Applications" (page 37)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/iHTML_Based_Applications.html)).
The process is different for creating a Java Client application
or applet. Instead of using WebObjects Builder to create the user interface,
you use an application called Interface Builder.

|  |
| --- |
| __Note:__ If you're familiar with Cocoa development, the process for creating a Java Client user interface is nearly the same as the one for creating a Cocoa user interface for Mac OS X applications. |

In Interface Builder, you typically construct a user interface
by dragging widgets from a palette and dropping them into a window,
as shown in [Figure 6-5](#apple-ijauussgjjcem). It does more, however, than simple user interface
layout. Interface Builder also lets you create, edit, and connect objects
so they can communicate with one another at runtime.

__Figure
6-5 Composing a user interface with Interface
Builder__

![[image: ../Art/IB.gif]](../Art/IB.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Other_Architectures.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Advantages__nt_Approach.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

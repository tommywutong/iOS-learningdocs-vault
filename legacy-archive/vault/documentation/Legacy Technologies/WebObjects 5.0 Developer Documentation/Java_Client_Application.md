---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Overview/Java_Client_Application.html
archived_at: '2026-07-15T08:14:36.621127Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Java_Client_Architecture.md)[![Next](attachments/JavaClient/Images/next.gif)](Java_Client_and_Classes.md)

## Java Client as a WebObjects Application

Out of the box, Java Client runs as a type of WebObjects application.
In the multi-tier architecture described earlier, WebObjects provides
an application server as well as HTML and HTTP support. The distribution
layer on the client provides an HTTP channel to handle communication
between the application server and the Java Client application.

A Java Client WebObjects application gives you considerable
flexibility in how you compose the pages of your application. However,
it is strongly recommended that your Java Client projects be executed
on the client as stand-alone applications instead of applets. By
doing this, you avoid the many compatibility issues present when
running applets inside different browsers. However, if your business
requires that your project use applets on the client instead of
applications, you can combine Java Client applets and static and dynamic
(WebObjects) HTML elements in various ways. You can have pages with
or without Java Clients or pages with multiple Java Clients, each
with its own controller. For example, you could have a login page
that takes the user to one of many Java Client pages based on some
piece of account data. In addition, Java Client applets are not
limited to the downloaded JFC components; as can any applet, they
can create dialogs and secondary windows on the fly.

When you create a Java Client project using Project Builder,
the project is organized using three targets:

- The Web Server
  target, which lists the files required to build the client application.

  This
  target contains an interface file that stores an archive of J2SE
  (and other 100% Pure Java) objects. That file's owner is a custom
  subclass of EOInterfaceController. For more on Interface Builder
  see ["Creating the User Interface"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/iCreating_th_r_Interface.html).
- The Application Server target, which lists the files needed
  to build the server application.

  This target includes the `Main.wo` component
  that contains a subcomponent of type WOJavaClientApplet. Also included
  are the `Application`, `Session`,
  and `DirectAction` classes.
- The root target, named after the project, which groups the
  Client and Server targets. It is used to build the entire project
  (the Client and Server products) as a single unit.

For more on Project Builder's targets see ["File Organization in Project Builder"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/iThe_Ingredi_ent_Project.html).

The frameworks required to build a Java Client application
are also automatically added to your project.

When you launch the client side of a Java Client application
(an application or an applet), the server application creates a
WOSession object. It contains the EOEditingContext and EODistributionContext
objects used to manage enterprise objects (read from and write to a
database) and to synchronize them with their counterparts on the
client.

With Java Client applets, the client automatically downloads
the classes that it needs to run from the server if they are not
already installed on the client's classpath. This way the client-side
applet is always updated. There are several disadvantages with this
approach:

- __Longer
  application launch times__ Launch times suffer because
  the client has to make sure that the appropriate classes are installed
  before the applet can run.
- __Security restrictions__ Browsers impose
  restrictions on the actions that downloaded code can perform on
  the client machine (those restrictions can be modified or removed by
  editing preference settings in the browser).
- __Application instability__ Java Virtual
  Machine (VM) implementations in browsers are generally poor. When
  more than one applet are run inside a browser, they often share the
  same VM, contributing to application instability.

When the client-side applications are executed as applications
instead of applets, launch times are minimized because the server
sends only data to the client, not class implementations. However,
when a new version of an application is developed, the client needs
to be manually upgraded; otherwise, an exception is thrown when
the user tries to run the application.

As you can see from the diagram in [Figure 1-3](#apple-ijbusssfijfem), each session created
and managed by the WebObjects application has, if it is communicating
with a Java Client application, its own editing context and its
own server-side distribution layer. As described earlier, communication
between the server and client is handled through the distribution
layers on the server and the client. The WOApplication maintains
the object store (EODatabaseContext) for all its sessions.

__Figure
1-3 Java Client in a WebObjects application__

![[image: ../Art/javaclientinwoapp.gif]](../Art/javaclientinwoapp.gif)

The session object is, by default, the delegate of the distribution
layer's EODistributionContext, the object that handles communication
on the server. The EODistributionContext class defines several security-related
delegate methods for validating remote invocations; if you wish,
you can simply implement these methods in your Session class.

[![Previous](attachments/JavaClient/Images/previous.gif)](Java_Client_Architecture.md)[![Next](attachments/JavaClient/Images/next.gif)](Java_Client_and_Classes.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

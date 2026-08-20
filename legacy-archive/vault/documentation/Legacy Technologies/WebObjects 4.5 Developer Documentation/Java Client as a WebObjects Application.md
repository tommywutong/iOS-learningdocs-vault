---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.5.html
archived_at: '2026-07-15T08:09:17.109281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Overview%20of%20Java%20Client.md) [!](Data%20Synchronization%20Between%20Client%20and%20Server.md) [!](Java%20Client%20Layers%20and%20Classes.md)

---

# Java Client as a WebObjects Application

Out of the box, Java Client runs as a type of WebObjects application. In the multi-tier architecture described earlier, WebObjects provides an application server as well as HTML and HTTP support. The distribution layer on the client provides an HTTP channel to handle communication between the application server and the Java Client applets in client Web pages.

A Java Client WebObjects application gives you considerable flexibility in how you compose the pages of your application. You can combine Java Client applets and static and dynamic (WebObjects) HTML elements in various ways. You can have pages with or without Java Clients or pages with multiple Java Clients, each with its own controller. For example, you could have a login page that takes the user to one of many Java Client pages based on some piece of account data. In addition, Java Client applets are not limited to the downloaded JFC components; as can any applet, they can create dialogs and secondary windows on the fly.

When you create a Java Client project using Project Builder, two things of specific interest (in terms of Java Client) are created for you:

- 

  A subproject of type EOJavaClientSubproject named, by default, __ClientSideJava.subproj__. This subproject contains an Interface Builder "nib" (or interface) file whose file's owner is a custom subclass of EOInterfaceController.
- 

  A __Main.wo__ component which contains a subcomponent of type WOJavaClientApplet.

The EOJavaClientFramework is also automatically added to your project.

In an EOJavaClientSubproject, when you create a user interface using Interface Builder, the nib file stores an "archive" of JFC (and other 100% Pure Java) objects. Also in the subproject are the interface controller and any other custom enterprise-object or other classes that you have implemented in Java.

WOJavaClientApplet is a component that is used to download and create an applet of class com.apple.client.interface.EOApplet. It has a dozen or so potential bindings, some general to applets (such as codebase and size) and others specific to Java Client (such as distribution-channel class and interface-controller class).

When you launch a Java Client application, a WebObjects application (__.woa__) instance is started on the server. Whenever a client requests a page of this application that has a WOJavaClientApplet, the __.class__ files implementing the required objects are downloaded to the page and installed on the client. The applet is loaded and started and the user is ready to fetch, add, delete, and modify data.

As you can see from the diagram in [Java Client in a WebObjects Application](#apple-geydkmzy)
, each session created and managed by the WebObjects application has, if it is communicating with a Java Client application, its own editing context and its own server-side distribution layer. As described earlier, communication between the server and client is handled through the distribution layers on the server and the client. The WOApplication maintains the object store (EODatabaseContext) for all sessions.

!

__Figure 1-3__  Java Client in a WebObjects Application

The session object is, by default, the delegate of the distribution layer's EODistributionContext, the object that handles communication on the server. The EODistributionContext class defines several security-related delegate methods for validating remote invocations; if you wish, you can implement these methods in your Session class.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Overview%20of%20Java%20Client.md) [!](Data%20Synchronization%20Between%20Client%20and%20Server.md) [!](Java%20Client%20Layers%20and%20Classes.md)

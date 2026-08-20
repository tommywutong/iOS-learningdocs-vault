---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.8a.html
archived_at: '2026-07-15T08:00:04.349023Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.8.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.9.md)

## Tutorial

This tutorial shows you how to create a "Java Client" WebObjects application, which is a distributed Enterprise Objects Framework application that uses a Web browser as its display medium. The application is "distributed" in the sense that business logic can be shared among enterprise objects on the Web client (which are implemented in Java) and enterprise objects on the server (which can be implemented in Java or Objective-C). The steps you take to create a Java Client WebObjects application are remarkably similar to the steps you take to create a typical stand-alone (or "fat client") Enterprise Objects Framework application.

The application you'll be creating in this chapter, StudioManager, is based on the Movies sample database distributed with Enterprise Objects Framework (you must have the sample databases installed to do this tutorial). It centers around three types of enterprise objects: Studio, Movie, and Talent. StudioManager own movies, and they have a budget for buying new movies. Movies feature actors, or "talent." The StudioManager application lets you transfer movies between studios and buy all of the movies starring a particular actor. It also lets you add, modify, and delete studios.

The StudioManager example project upon which this tutorial is based is installed in _NEXT_ROOT_
__/Developer/Examples/WebObjects/JavaClient__
.

####  Requirements

To run the StudioManager application, or any Java Client application, you must have server and client systems with certain capabilities beyond the usual requirements for Enterprise Objects Framework applications (database servers, for instance). You must have a client (such as a Web browser) and a server platform that implement Java virtual machines (VM) on which "100% pure Java" applications can run. The client must also support the following standards:

- Java Foundation Classes (JFC), also known as "Swing"
  - A transport layer such as HTTP or CORBA,

    Currently, Java Client applications can be run from Microsoft Internet Explorer and Netscape browsers (with the Java Plug-in from SunSoft), and with the JDK's __appletviewer__
    and __java__
    programs.

  __Related Concepts:__ Java Client Architectural Overview

  ###### 

  !

  ---

  \xA9 1999 Apple Computer, Inc.

  [Previous](CSJ_Tutorial.8.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.9.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)

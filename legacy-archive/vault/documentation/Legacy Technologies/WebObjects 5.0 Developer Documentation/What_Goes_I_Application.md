---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/What_Goes_I_Application.html
archived_at: '2026-07-15T08:14:19.681254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Enterprise__l_Databases.md)[![Next](attachments/JavaClient/Images/next.gif)](Creating_the_Movies_Model.md)

## What Goes Into the Studio Manager Application

As with most Java Client WebObjects applications, you create
the Java Client Studio Manager application using the following ingredients:

- __A model
  of the WOMovies database__ A model defines a mapping between
  your enterprise objects and data in a relational database. See ["What Is a Model?"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/iWhat_Is_a_Model_.html) for
  additional information.
- __A user-interface__ You use Interface
  Builder to construct a Swing/J2SE-based user-interface that can
  interact with the user. In Interface Builder's Preferences, you must
  load a special palette (`EnterpriseObjects.palette`)
  located in `/Developer/Palettes`.
  With Interface Builder you can compose a user interface made from "widgets"
  derived from the Java Foundation Classes (JFC), informally known
  as Swing.
- __Web Components__ The Main component is
  automatically set up to have a WOJavaClientApplet component that
  is bound to the interface controller on the client. You can add
  other Web components with or without a Java Client linkage. Also provided
  are skeletal implementation files for the server-side application,
  session, and direct-action objects as well as API bindings files
  for server-side components.
- __Source code for custom enterprise object classes__ In
  the Studio Manager application, these are Studio and Talent. Movie
  uses the default enterprise object class, EOGenericRecord, since
  it has no custom behavior. This is described in more detail in later
  sections.

In addition, the Studio Manager application requires a database
server on which you've installed the WOMovies example database.
The final ingredients in the application are the Enterprise Objects
Framework, WebObjects and Foundation classes, interfaces, and protocols,
which you link into your application.

See ["What Is an Enterprise Object?"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/iWhat_Is_an__ise_Object_.html) for
more information on enterprise objects.

[![Previous](attachments/JavaClient/Images/previous.gif)](Enterprise__l_Databases.md)[![Next](attachments/JavaClient/Images/next.gif)](Creating_the_Movies_Model.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

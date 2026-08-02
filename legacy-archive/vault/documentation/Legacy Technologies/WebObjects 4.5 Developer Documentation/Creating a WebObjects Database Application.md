---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.25.html
archived_at: '2026-07-15T08:07:26.449812Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Getting%20Started%20With%20WebObjects.md) [!](Adding%20a%20Dynamic%20Hyperlink.md) [!](The%20Movies%20Application.md)

---

#   Creating a WebObjects Database Application

One of the most powerful features of WebObjects is its ability to provide access to databases. To do so, it uses a framework called the Enterprise Objects Framework. This chapter introduces you to the Enterprise Objects Framework by showing you how to create a simple database application. The steps you take in creating this application demonstrate the principles you'll use in every other application you develop with the WebObjects and Enterprise Objects frameworks.

The application you'll create in this tutorial is called Movies. It makes use of a sample database, the Movies database, that contains information about movies. In this tutorial we'll use the OpenBase Lite database that comes with WebObjects. If you wish to use another database, you need to set up the Movies database as described in the Post-Installation Instructions. Also, if you aren't familiar with Project Builder and WebObjects Builder, read the first tutorials in this book, [Creating a Simple WebObjects Application](Creating%20a%20Simple%20WebObjects%20Application.md#apple-gmzdiobz)
and [Enhancing Your Application](Enhancing%20Your%20Application.md#apple-gmytmnrq)
, which introduce basic concepts and procedures you should know before you go on.

In this tutorial, you will:

- 

  Use the WebObjects Application Wizard to create a fully functional Main component that reads and writes from the Movies database.
- 

  Create and configure _display groups_ for interacting with a database in terms of objects.
- 

  Create bindings between display groups and a user interface.
- 

  Write code to manipulate display groups' selected objects.
- 

  Set up display groups in a master-detail configuration.
- 

  Use EOModeler to maintain a model file.
- 

  Create custom enterprise object classes.

Along the way, you'll learn basic Enterprise Objects Framework concepts you can use to design your own database applications.
__Note:__

You can also develop database applications using Direct to Web, a high-level framework based on WebObjects. Direct to Web instantly generates a generic database application and allows you to modify its user interface, which makes it a useful starting point for simple projects without very specific user interface requirements. See _WebObjects Tools and Techniques_ and _Developing WebObjects Applications With Direct to Web_ for more information.

#### [The Movies Application](The%20Movies%20Application.md#apple-obtwmslehuytsnbyhe)

#### [Enterprise Objects and the Movies Database](Enterprise%20Objects%20and%20the%20Movies%20Database.md#apple-obtwmslehuytcmbvgy)

#### [Designing the Main Page](Designing%20the%20Main%20Page.md#apple-obtwmslehuytknjxhe)

#### [Examining Your Project](Examining%20Your%20Project-2.md#apple-obtwmslehuztamy)

#### [Refining Main.wo](Refining%20Main.wo.md#apple-obtwmslehuytgnjug4)

#### [Adding the MovieDetails Page](Adding%20the%20MovieDetails%20Page.md#apple-obtwmslehuzdmmjrgy)

#### [Refining Your Model](Refining%20Your%20Model.md#apple-obtwmslehu2dina)

#### [Setting Up a Master-Detail Configuration](Setting%20Up%20a%20Master-Detail%20Configuration.md#apple-obtwmslehuytgnzwg4)

#### [Updating Objects in the Detail Display Group](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md#apple-obtwmslehu2tomq)

#### [Adding Behavior to Your Enterprise Objects](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md#apple-obtwmslehuytsmjrga)

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Getting%20Started%20With%20WebObjects.md) [!](Adding%20a%20Dynamic%20Hyperlink.md) [!](The%20Movies%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

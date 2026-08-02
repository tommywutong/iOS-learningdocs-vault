---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.57x.html
archived_at: '2026-07-15T08:11:01.228745Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Reusable%20Components.md) [!](Creating%20a%20Direct%20to%20Web%20Project.md)

---

# Direct to Web

Direct to Web is a Java-based technology that provides a quick and easy method to create a web application that accesses a database. It lets you experiment and prototype, while also allowing you the flexibility to access the full power of WebObjects.

There are several stages you can go through, depending on your needs:

- 

  First, you create a WebObjects project and specify a _model_
  to use. Direct to Web uses the model, which defines the mapping between your database and enterprise object classes, to generate an application that provides an interface to your database. This application consists of a set of pages that allow you to do queries on the entities in your database, display results, and add and delete records.

  A complete and correct model file with all the right relationships defined is key to creating a WebObjects application with Direct to Web.
- 

  To change the way the pages are presented, you can use the Direct to Web Assistant (Web Assistant for short), which is a Java applet that runs in your web browser. For each page in your application, the Web Assistant allows you to specify which pages are shown, which properties are shown, how these properties are displayed, and the order in which they are listed. You can experiment with different configurations until you are satisfied, without writing any code.
- 

  If you want to do customize beyond what the Web Assistant provides, you can "freeze" any or all of the pages in your application as WebObjects components. This gives you the full power of WebObjects: you can modify a component's layout using WebObjects Builder, and you can customize its behavior by writing Java code using Project Builder.
- 

  You can also modify the templates which Direct to Web uses to generate its pages. These templates are WebObjects components that you can edit with WebObjects Builder. This way you can modify the "look" or style of the pages that Direct to Web generates.

You can also use Direct to Web in other types of WebObjects applications. Your application can take two approaches:

- 

  Embedding Direct to Web components in your pages; these include query forms, lists, or edit/inspect forms.
- 

  Linking to dynamically generated Direct to Web pages

This document describes the elements that make up a Direct to Web application, and shows you the steps you follow when creating and modifying an application. If you find that your application needs some specific behavior that Direct to Web does not provide, see _Developing WebObjects Applications with Direct to Web_
. For more information about using Project Builder and WebObjects Builder to develop WebObjects applications, see _WebObjects Tools and Techniques_
. For more information about using WebObjects with database applications, see "Creating a WebObjects Database Application" in _Getting Started With WebObjects_
, as well as the Enterprise Objects Framework Developer's Guide.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Reusable%20Components.md) [!](Creating%20a%20Direct%20to%20Web%20Project.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

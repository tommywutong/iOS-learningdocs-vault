---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/An_Introduc_rect_To_Web.html
archived_at: '2026-07-15T08:12:23.741396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Introduction/iAbout_This_Book.html)[!](Creating_a__Web_Project.md)

# An Introduction to Direct To Web

Direct to Web is a Java-based technology that provides a
quick and easy method to create a web application that accesses a database. It
lets you experiment and prototype, while also allowing you the flexibility to
access the full power of WebObjects.

There are
several stages you can go through, depending on your needs:

- First, you create a WebObjects project and specify a _model_ to
  use. Direct to Web uses the model, which defines the mapping between your
  database and enterprise object classes, to generate an application that provides
  an interface to your database. This application consists of a set of pages that
  allow you to do queries on the entities in your database, display results, and
  add and delete records.

  A complete model file that correctly defines all the
  relationships is the key to creating a WebObjects application with Direct to Web.
- To change the way the pages are presented, you can use the
  WebAssistant, which is a Java applet that runs in your web browser. For each page
  in your application, the WebAssistant allows you to specify which page is shown,
  which properties are shown on the page, how these properties are displayed, and
  the order in which they are listed. You can experiment with different
  configurations until you are satisfied, without writing any code.
- If you want to customize beyond what the WebAssistant provides, you can
  "freeze" any or all of the pages in your application as WebObjects components.
  This gives you the full power of WebObjects: you can modify a component's layout
  using WebObjects Builder, and you can customize its behavior by writing Java code
  using Project Builder.
- You can also modify the templates that
  Direct to Web uses to generate its pages. These templates are WebObjects
  components that you can edit with WebObjects Builder. This way you can modify the
  "look" or style of the pages that Direct to Web generates.

You can also use Direct to Web in other types of WebObjects
applications. Your application can take two approaches:

- embedding Direct to Web components in your pages; these include query
  forms, lists, or edit/inspect forms
- linking to dynamically
  generated Direct to Web pages

This chapter
describes the elements that make up a Direct to Web application, and shows you
the steps you follow when creating and modifying an application. If you find that
your application needs some specific behavior that Direct to Web does not
provide, see ["Customizing a
Direct to Web Application"](../Customizing/Customizing_Application.md#apple-ijauessdizfec). For more information about using Project Builder
and WebObjects Builder to develop WebObjects applications, see _WebObjects
Tools and Techniques_. For more information about using WebObjects with
database applications, see "Creating a WebObjects Database Application" in
_Getting Started With WebObjects_, as well as the _Enterprise Objects
Framework Developer's Guide_.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Introduction/iAbout_This_Book.html)[!](Creating_a__Web_Project.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

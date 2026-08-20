---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.html
archived_at: '2026-07-15T07:53:12.499199Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](../WebObjectsTOC.md)[Top](../WebObjectsTOC.md)

# Direct To Web

---

Direct to Web is a technology that provides a quick and easy method of creating a web application that accesses a database. It lets you experiment and prototype, while also allowing you the flexibility to access the full power of WebObjects.

There are several stages you can go through, depending on your needs:

- 

  First, you create a WebObjects project and specify a _model_
  to use. Direct to Web uses the model, which defines the mapping between your database and enterprise object classes, to generate an application that provides an interface to your database. This application consists of a set of pages that allow you to do queries on the entities in your database, display results, and add and delete records.
- 

  To change the way the pages are presented, you can use the WebAssistant, which is a Java applet that runs in your web browser. For each page in your application, you can specify which properties are shown, how they are displayed, and the order in which they are listed. You can experiment with different configurations until you are satisfied, without writing any code.
- 

  If you want to do further customization beyond what the WebAssistant provides, you can "freeze" any or all of the pages in your application as WebObjects components. This gives you the full power of WebObjects: you can modify a component's layout using WebObjects Builder, and you can customize its behavior by writing Java code using Project Builder.

This document describes the elements that make up a Direct to Web application, and shows you the steps you follow when creating and modifying an application. See _WebObjects Tools and Techniques_
for more information on using Project Builder and WebObjects Builder to develop WebObjects applications. For more information about using WebObjects with database applications, see "Creating a WebObjects Database Application" in _Getting Started With WebObjects_
, as well as the _Enterprise Objects Framework Developer's Guide_.

---

**# Table of Contents**

## [Creating a Direct to Web Project](DirectToWeb.1.md#apple-obtwmslehu4teobt)

## [The Structure of a Direct to Web Project](DirectToWeb.2.md#apple-obtwmslehu3tgnjv)

## [Using Your Direct to Web Application](DirectToWeb.3.md#apple-obtwmslehu2tembv)

: ### [The Login Page](DirectToWeb.4.md#apple-obtwmslehu4dknjs)

### [Query Pages](DirectToWeb.5.md#apple-obtwmslehu2tcnjv)

### [List Pages](DirectToWeb.6.md#apple-obtwmslehu4dambs)

### [Inspect and Edit Pages](DirectToWeb.7.md#apple-obtwmslehu2tcnrv)

## [Customizing Your Application With WebAssistant](DirectToWeb.8.md#apple-obtwmslehu2tqmjx)

: ### [The Direct to Web Components](DirectToWeb.9.md#apple-obtwmslehu4danjx)

: ### [WebAssistant Expert Mode](DirectToWeb.a.md#apple-obtwmslehu4danju)

## [Generating Components](DirectToWeb.b.md#apple-obtwmslehu3domrx)

## [Modifying Your Application's Code](DirectToWeb.c.md#apple-obtwmslehu4dcnby)

---

[!](DirectToWeb.1.md)[First
Section](DirectToWeb.1.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

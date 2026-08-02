---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb.html
archived_at: '2026-07-15T08:01:40.478773Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Reusable%20Components.md)

# Direct To Web

---

Direct to Web is a technology that provides a quick and easy method of creating a web application that accesses a database. It lets you experiment and prototype, while also allowing you the flexibility to access the full power of WebObjects.
There are several stages you can go through, depending on your needs:

- First, you create a WebObjects project and specify a _model_ to use. Direct to Web uses the model, which defines the mapping between your database and enterprise object classes, to generate an application that provides an interface to your database. This application consists of a set of pages that allow you to do queries on the entities in your database, display results, and add and delete records.

A complete and correct model file with all the right relationships defined is key to creating a WebObjects application with Direct to Web.

- To change the way the pages are presented, you can use the WebAssistant, which is a Java applet that runs in your web browser. For each page in your application, the WebAssistant allows you to specify which pages are shown, which properties are shown, how these properties are displayed, and the order in which they are listed. You can experiment with different configurations until you are satisfied, without writing any code.
- If you want to do further customization beyond what the WebAssistant provides, you can "freeze" any or all of the pages in your application as WebObjects components. This gives you the full power of WebObjects: you can modify a component's layout using WebObjects Builder, and you can customize its behavior by writing Java code using Project Builder.

You can also use Direct to Web in other types of WebObjects applications. Your application can take two approaches:

- Embedding Direct to Web components in your pages; these include query forms, lists, or edit/inspect forms.
- Linking to dynamically generated Direct to Web pages

This document describes the elements that make up a Direct to Web application, and shows you the steps you follow when creating and modifying an application. See _[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)_ for more information on using Project Builder and WebObjects Builder to develop WebObjects applications. For more information about using WebObjects with database applications, see "[Creating a WebObjects Database Application](Creating%20a%20WebObjects%20Database%20Application.md)" in _Getting Started With WebObjects_, as well as the _Enterprise Objects Framework Developer's Guide._

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Creating%20a%20Direct%20to%20Web%20Project.md)

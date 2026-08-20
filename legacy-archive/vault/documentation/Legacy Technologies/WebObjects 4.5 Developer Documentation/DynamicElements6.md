---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements6.html
archived_at: '2026-07-15T08:05:29.967047Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](Client-Side%20Java%20Components.md)

## Dynamic Elements vs. Client-Side Components

Although an application constructed using client-side components aren't nearly as powerful or flexible as one constructed with a pure Java Client interface, client-side components do give you greater control over the appearance of your application when compared to an application that uses only dynamic elements and static HTML elements in its interface. When compared only against server-side dynamic elements, client-side components have these advantages:

- Client-side components allow you to update UI elements without reloading the page.

WebObjects applications are event driven. The events that trigger actions are HTTP requests. A WebObjects application receives an HTTP request from the client, processes it, and returns a response page. That is, the only communication that takes place between the client and the WebObjects application on the server results in a page being redrawn (or a new page being generated).

When client-side components are used, an HTTP request can result in either the re-synchronization of state or the return of a new page. Thus, state can be synchronized without the page having to be redrawn (see [Figure 13](#apple-gmztgmy)).

!

Figure 13. Client-Side Java Components

- Client-side components are more flexible than server-side dynamic elements.

Server-side dynamic elements always generate HTML, which means that they are limited to what HTML looks like and what HTML can do. You can create client-side components that look like just about any imaginable control: a dynamic calendar, a spreadsheet, or a graphing tool.

One disadvantage to using client-side components is that they require a Java-enabled browser. Thus, you can use client-side components only when you can be certain all of your users will have Java-enabled browsers. If you can't guarantee this, you should limit your application to server-side dynamic elements.

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements7.md)

---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/DynEl/DecidingToUse.html
archived_at: '2026-07-15T07:51:30.095625Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](ClientSide.md)

## Deciding When to Use Client-Side Components

You should use client-side components whenever you want greater control over the appearance of your application. In general, client-side components have these advantages over server-side dynamic elements:

- Client-side components define a state-synchronization phase that does not reload the page.

As you learned in the first chapter, WebObjects applications are event driven. The events that trigger actions are HTTP requests. A WebObjects application receives an HTTP request from the client, processes it, and returns a response page. That is, the only communication that takes place between the client and the WebObjects application on the server results in a page being redrawn (or a new page being generated).

When client-side components are used, an HTTP request can result in either the resynchronization of state or the return of a new page. Thus, state can be synchronized without the page having to be redrawn (see [Figure 13](#apple-gmztgmy)).

!Figure 13. Client-Side Java Components- Client-side components are more flexible than server-side dynamic elements.

Server-side dynamic elements always generate HTML, which means that they are limited to what HTML looks like and what HTML can do. You can create client-side components that look like just about any imaginable control: a dynamic calendar, a spreadsheet, or a graphing tool. To learn how to create a client-side component, see the chapter ["Creating Client-Side Components"](../ClientSide/ClientSideTOC.md).

The disadvantage to using client-side components is that they require a Java-enabled browser. Thus, you can use client-side components only when you can be certain all of your users will have Java-enabled browsers. If you can't guarantee this, you should use server-side dynamic elements.

[!Table of Contents](DynElTOC.md) [!Next Section](HowClientSideWork.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

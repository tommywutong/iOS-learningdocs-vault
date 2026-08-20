---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/RRLoopInfo.html
archived_at: '2026-07-15T07:51:51.394170Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](SessionMgmt.md)

## Request Level

The request-response cycle has three phases, the first for transferring user-entered data to the objects associated with the request page, the second for invoking an action method, and the third for generating and returning the response. [Figure 16](#apple-he4a) shows how WebObjects requests are handled at the transaction level.

!Figure 16. Request-Response Loop: Transaction Level
Three classes are involved at this level:

- WORequest (in Java, Request)

Stores essential data about an HTTP request, such as header information, form values, HTTP version, host and page name, and session, context, and sender IDs.

- WOResponse (in Java, Response)

Stores and allows the modification of HTTP response data, such as header information, status, and HTTP version. It also provides convenience methods for appending HTML and simple textual data to the content of the response (that is, the response page).

- WOContext (in Java, Context)

Provides access to the objects involved in the current cycle, such as the current request, response, session, and application objects. It also stores the component (either the current page or one of its subcomponents) to which the elements of the page make reference when they "push and pull" values through association. See ["How HTML Pages Are Generated"](ComponentElement.md#apple-gy2dsmq) for an explanation. The WOContext object acts as a "cursor," traversing the object graph during each phase of the request-response loop. The WOContext for a cycle is identified by a unique context ID, which appears in the URL.

You rarely need to work directly with WORequest, WOResponse, and WOContext yourself. At the beginning of the request-response loop, the WOAdaptor and WOApplication objects create instances of these three classes. The application initiates each phase of the request-response loop by sending the messages __takeValuesFromRequest:inContext:__, __invokeActionForRequest:inContext:__, and __appendToResponse:inContext:__ (in Java, __takeValuesFromRequest__, __invokeAction__, and __appendToResponse__). It passes in the WORequest, WOResponse, and WOContext objects as arguments to one or more of these methods. From these objects, the components, dynamic elements, and other objects involved in the cycle get essential information. See ["How WebObjects Works-A Class Perspective"](PhasesRRLoop.md#apple-gezti) for more on the mechanics of request handling.

[!Table of Contents](HowWOWorks.md) [!Next Section](PageComp.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

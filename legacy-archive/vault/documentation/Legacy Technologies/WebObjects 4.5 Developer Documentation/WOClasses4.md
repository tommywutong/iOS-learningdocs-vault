---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses4.html
archived_at: '2026-07-15T08:06:20.632721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses3.md)

## Request Level

The request-response cycle has three phases, the first for transferring user-entered data to the objects associated with the request page, the second for invoking an action method, and the third for generating and returning the response. [Figure 17](#apple-he4a) shows how WebObjects requests are handled at the transaction level.

!

Figure 17. Request-Response Loop: Transaction Level

Three classes are involved at this level:

- WORequest

Stores essential data about an HTTP request, such as header information, form values, HTTP version, host and page name, and session, context, and sender IDs.

- WOResponse

Stores and allows the modification of HTTP response data, such as header information, status, and HTTP version. It also provides convenience methods for appending HTML and simple textual data to the content of the response (that is, the response page).

- WOContext

Provides access to the objects involved in the current cycle, such as the current request, response, and session objects. It also stores the current component (either the current page or one of its subcomponents) to which the elements of the page make reference when they "push and pull" values through associations. See ["How HTML Pages Are Generated"](How%20HTML%20Pages%20Are%20Generated.md#apple-haytioa) for an explanation. The WOContext object acts as a "cursor," traversing the object graph during each phase of the component action request-response loop. The WOContext for a cycle is identified by a unique context ID.

You rarely need to work directly with WOContext, and only occasionally with WORequest and WOResponse. At the beginning of the request-response loop, the WOAdaptor and WORequestHandler objects create instances of these three classes and they are passed from object to object as needed. From these objects, the components, dynamic elements, and other objects involved in the cycle get essential information. See ["How WebObjects Works-A Class Perspective"](How%20WebObjects%20Works-A%20Class%20Perspective.md#apple-gezti) for more on the mechanics of request handling.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses5.md)

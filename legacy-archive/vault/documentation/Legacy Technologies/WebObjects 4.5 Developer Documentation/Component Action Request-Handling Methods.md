---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods12.html
archived_at: '2026-07-15T08:05:51.209809Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods11.md)

# Component Action Request-Handling Methods

By default, your application uses the component action request handling loop. (["Setting the Default Request Handler"](Methods5.md#apple-ha3tanq) shows you how to make the direct action request handling loop the default for your application.) Component action request handling is performed in three phases, which correspond to three methods you can override:

- Taking input values from the request (__takeValuesFromRequest:inContext:__ or __takeValuesFromRequest__)
- Invoking the action (__invokeActionForRequest:inContext:__ or __invokeAction__)
- Generating a response (__appendToResponse:inContext:__ or __appendToResponse__)

Each of the methods is implemented by WOApplication, WOSession, and WOComponent. In each phase, WOApplication receives the message first, then sends it to the WOSession, which sends it to the WOComponent, which sends it to all of the dynamic element and component objects on the page.
The request-handling methods handle three types of objects:

- A request object (WORequest) is passed as an argument in the first two phases. This object represents a user request. You can use it to retrieve information about the request, such as the method line, request headers, URL, and form values.
- A context object (WOContext) is passed as an argument in all three phases. This object represents the current context of the request. It contains references to information specific to the request, such as the current component, current session, and current request.
- A response object (WOResponse) is passed in the final phase. This object encapsulates information contained in the generated HTTP response, such as the status, response headers, and response content.

You should override these methods if you need to perform a task that requires this type of information or you need access to objects before or after the action method is invoked. For example, if you need to modify the header lines of an HTTP response or substitute a page for the requested page, you would override __appendToResponse:inContext:__.
As you implement request-handling methods, you must invoke the superclass's implementation of the same methods. But consider _where_ you invoke it because it can affect the request, response, and context information available at any given point. In short, you want to perform certain tasks before __super__ is invoked and other tasks after __super__ is invoked.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods13.md)

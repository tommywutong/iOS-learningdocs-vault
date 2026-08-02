---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/RequestHandlingMethods.html
archived_at: '2026-07-15T07:51:15.993842Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](ComponentInit.md)

# Request-Handling Methods

Request-handling is performed in three phases, which correspond to three methods that you can override:

- Taking input values from the request (__takeValuesFromRequest:inContext:__ or __takeValuesFromRequest__)
- Invoking the action (__invokeActionForRequest:inContext:__ or __invokeAction__)
- Generating a response (__appendToResponse:inContext:__ or __appendToResponse__)

Each of the methods is implemented by WOApplication, WOSession, and WOComponent. In each phase, WOApplication receives the message first, then sends it to the WOSession, which sends it to the WOComponent, which sends it to all of the dynamic element and component objects on the page.
The request-handling methods handle three types of objects:

- A request object (WORequest or Request in Java) is passed as an argument in the first two phases. This object represents a user request. You can use it to retrieve information about the request, such as the method line, request headers, the URL, and form values.
- A context object (WOContext or Context in Java) is passed as an argument in all three phases. This object represents the current context of the application. It contains references to information specific to the application, such as the path to the request component's directory, the version of WebObjects that's running, the application name, and the request page's name.
- A response object (WOResponse in Java) is passed in the final phase. This object encapsulates information contained in the generated HTTP response, such as the status, response headers, and response content.

You should override these methods if you need to perform a task that requires this type of information or you need access to objects before or after the action method is invoked. For example, if you need to modify the header lines of an HTTP response or substitute a page for the requested page, you would override __appendToResponse:inContext:__.
As you implement request-handling methods, you must invoke the superclass's implementation of the same methods. But consider _where_ you invoke it because it can affect the request, response, and context information available at any given point. In short, you want to perform certain tasks before __super__ is invoked and other tasks after __super__ is invoked.

[!Table of Contents](CommonMethods.md) [!Next Section](takeValuesFromRequest.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

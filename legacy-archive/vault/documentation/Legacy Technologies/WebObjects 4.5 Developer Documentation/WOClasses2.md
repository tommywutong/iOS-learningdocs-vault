---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses2.html
archived_at: '2026-07-15T08:06:16.130123Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](The%20Classes%20in%20the%20Request-Response%20Loop.md)

## Server and Application Level

At the server and application level, the request-response loop looks like that shown in [Figure 15](#apple-giztemq).

!

Figure 15. Request-Response Loop: Application and Server Level

The HTTP server forwards a request to the application's adaptor. The adaptor packages the incoming HTTP request in a form the WebObjects application can understand and forwards it to the application. The application determines the type of the request (component action request or direct action request) and then forwards it to the appropriate request handler. The request handler manages the process of request handling and returns the completed response to the application, which passes it on to the adaptor, which gives it to the HTTP server in a form the server can understand.
Two classes are involved at this level:

- WOAdaptor

Defines the interface for objects mediating the exchange of data between an HTTP server and a WebObjects application. This is an abstract class.

- WOApplication

Receives requests from the adaptor, determines which request handler should handle the request, and forwards the request to that handler. After the request handler completes its processing, the application returns a response to the adaptor. WOApplication also creates dynamic elements "on the fly" and manages adaptors, sessions, application resources, and components.

- WORequestHandler

Manages the process of request handling and returns the completed response to the application. This is an abstract class.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses3.md)

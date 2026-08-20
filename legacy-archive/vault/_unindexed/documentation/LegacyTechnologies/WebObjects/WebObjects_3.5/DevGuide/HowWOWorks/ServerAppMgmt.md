---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/ServerAppMgmt.html
archived_at: '2026-07-15T07:51:52.945629Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](WideAngleView.md)

## Server and Application Level

At the server and application level, the request-response loop looks like that shown in [Figure 14](#apple-giztemq).

!Figure 14. Request-Response Loop: Application and Server Level
The HTTP server sends a request to the application's adaptor. The adaptor packages the incoming HTTP request in a form the WebObjects application can understand and forwards it to the application. The application initiates and manages the process of request handling and returns the completed response to the adaptor, which gives it to the HTTP server in a form the server can understand.
Two classes are involved at this level:

- WOAdaptor (in Java, Adaptor)

Defines the interface for objects mediating the exchange of data between an HTTP server and a WebObjects application. This is an abstract class.

- WOApplication (in Java, WebApplication)

Receives requests from the adaptor and initiates and coordinates the request-handling process, after which it returns a response to the adaptor. WOApplication also creates dynamic elements "on the fly" and manages adaptors, sessions, application resources, and components.

[!Table of Contents](HowWOWorks.md) [!Next Section](SessionMgmt.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

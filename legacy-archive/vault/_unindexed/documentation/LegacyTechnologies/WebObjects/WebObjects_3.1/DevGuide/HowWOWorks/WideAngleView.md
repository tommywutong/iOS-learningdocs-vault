---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/WideAngleView.html
archived_at: '2026-07-15T07:47:03.230648Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)

# __A Wide-Angle View of WebObjects__

WebObjects applications are event-driven, but instead of responding to mouse and keyboard events, they respond to HTTP requests. A WebObjects application receives a request, responds to it, then waits for the next request. The application continues to respond to requests until it terminates. On each cycle of this _request-response loop_, the application stores user input, invokes a method if one is associated with the user's action, and generates a response---usually an HTML page.

One way to get a sense of how WebObjects does this work is to survey incrementally the relationships and dynamics of the public classes. By learning about the basic role of each class, you can see how objects of that class fit into the mechanics of request handling.

Let's start the tour with the typical opening scenario: An incoming message (URL) from a client browser is handled by the HTTP server. From that point until an HTTP response is returned, WebObjects is working.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](ServerAppMgmt.md)

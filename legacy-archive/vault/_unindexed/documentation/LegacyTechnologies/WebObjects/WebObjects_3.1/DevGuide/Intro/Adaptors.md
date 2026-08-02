---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/Adaptors.html
archived_at: '2026-07-15T07:47:03.730835Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](ConnectingAppToWeb.md)

## WebObjects Adaptors

The WebObjects adaptor receives requests from the server, repackages the requests in a standard format, and forwards them to an appropriate WebObjects application. All WebObjects adaptors communicate with WebObjects applications in the same way, but they communicate with HTTP servers using whatever interface is provided by a particular server. For example, the WebObjects CGI adaptor uses the Common Gateway Interface, the Netscape Interface adaptor uses the Netscape Server API, and the Internet Server adaptor uses ISAPI. Thus, WebObjects adaptors can take advantage of server-specific interfaces but still provide server-independence.!Figure 4. The Role of a WebObjects Adaptor
By default, WebObjects uses the WebObjects CGI adaptor. The Common Gateway Interface is supported by all HTTP servers, so you can use the CGI adaptor with any server-including those that are publicly available. As performance demands increase, use one of the other adaptors with a server that supports the corresponding API (Netscape Server API or Internet Server API). Such servers are capable of dynamically loading the adaptor, eliminating the overhead of starting a new process for each request. As shown in [Figure 5](#apple-gmytkny), the communication between the adaptor and the HTTP server occurs inside a single process.

!Figure 5. The Netscape Interface Adaptor
The on-line document "[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/AboutWOAdmin.html)" describes how to configure a WebObjects adaptor.

[!Table of Contents](Start.book.md) [!Next Section](RoleOfExecutable.md)

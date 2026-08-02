---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/HTTPAdaptors.html
archived_at: '2026-07-15T07:55:54.066913Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](ServingWebObjectsTOC.md)

# WebObjects HTTP Adaptors

A key part of WebObjects administration is dealing with adaptors. This section provides a little background material on what a WebObjects HTTP adaptor is, how it works, and how you can configure it to suit your needs.
A WebObjects HTTP adaptor (called _WebObjects adaptor_ or sometimes _HTTP adaptor_) routes client requests processed by an HTTP server to WebObjects applications and returns the response to the server, which sends it back to the client. WebObjects makes available several adaptors, of which only one can be active with a particular server at a time. Every transaction with a WebObjects application uses the currently active adaptor.
However, the relationships between adaptor and application are (potentially) many-to-many. Multiple instances of the same WebObjects application can run on the same machine or a variety of machines and communicate with the same adaptor. In addition, multiple HTTP servers can be running on the same machine or on different machines; each server can have its own adaptor, each with its own constellation of application instances. Although there can be only one active HTTP adaptor per HTTP server, an application can concurrently communicate with other types of adaptors, such as an adaptor that uses Distributed Objects or a secure-socket adaptor.
There are two general types of HTTP adaptors:

- The CGI adaptor, an executable file named __WebObjects__ or __WebObjects.exe__ which resides in the host HTTP server's "cgi-bin" directory. This adaptor is available on all supported platforms. It is generic in that it works with any HTTP server conforming to the Common Gateway Interface (CGI).
- API-based adaptors, that is, adaptors based on APIs specific to particular web server. Three NSAPI adaptors, all based on the Netscape Server API (2.0, 2.0.1, and 3.0), are available on all supported platforms except Mach. A WebObjects adaptor based on Microsoft's Internet Information Server API (ISAPI) is also supported. The API-based adaptors have a performance advantage over CGI adaptors in that the associated server can dynamically load the adaptor; servers using CGI adaptors, on the other hand, spawn a new adaptor process for each request and kill the process after the response is provided.

When WebObjects is installed, the CGI adaptor is made active by default. To use an API-based adaptor, you must specifically activate it. Activating the API-based adaptor deactivates the CGI adaptor for a particular server. See "[Installing and Configuring NSAPI Adaptors](NSAPIConfig.md#apple-guytooi)" and "[Installing and Configuring the ISAPI Adaptor](ISAPIConfig.md#apple-guzdcna)" for further details.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](ConfigFiles.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/HTTPAdaptors.html
archived_at: '2026-07-15T07:49:55.239572Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)

# HTTP Adaptors

A WebObjects HTTP adaptor routes client requests processed by an HTTP server to WebObjects applications and returns the response to the server, which sends it back to the client. WebObjects makes available several HTTP adaptors, of which only one can be active with a particular server at a time. Every transaction with a WebObjects application uses the currently active HTTP adaptor.

However, the relationships between adaptor and application are (potentially) many-to-many. Multiple instances of the same WebObjects application can run on the same machine or a variety of machines and communicate with the same adaptor. In addition, multiple HTTP servers can be running on the same machine or on different machines; each server can have its own adaptor, each with its own constellation of application instances. Although there can be only one active HTTP adaptor per HTTP server, an application can concurrently communicate with other types of adaptors, such as an adaptor that uses Distributed Objects or a secure-socket adaptor.

There are two general types of HTTP adaptors. The first is the CGI adaptor, an executable file named __WebObjects__ or __WebObjects.exe__ which resides in the host HTTP server's "cgi-bin" directory. This adaptor is available on all supported platforms. It is generic in that it works with any HTTP server conforming to the Common Gateway Interface (CGI).

WebObjects also supports HTTP adaptors based on APIs specific to particular web servers. Three NSAPI adaptors, all based on the Netscape Server API (1.1, 2.0, and 2.0.1), are available on all supported platforms except Mach. An HTTP adaptor based on Microsoft's Internet Information Server API (ISAPI) is also supported. The API-based adaptors have a performance advantage over CGI adaptors in that the associated server can dynamically load the adaptor; servers using CGI adaptors, on the other hand, spawn a new adaptor process for each request and kill the process after the response is provided.

When WebObjects is installed, the CGI adaptor is made active by default. To use an API-based adaptor the WebObjects administrator must activate it. Activating the API-based adaptor deactivates the CGI adaptor for a particular server. See "[Installing and Configuring NSAPI Adaptors](NSAPIConfig.md#apple-kjcumobvgi3tm)" and "[Installing and Configuring the ISAPI Adaptor](ISAPIConfig.md#apple-kjcummzxgi4da)" for further details.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](ConfigFiles.md)

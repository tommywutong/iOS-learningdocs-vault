---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects3.html
archived_at: '2026-07-15T08:06:53.032830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](Java%20Client.md)

# How WebObjects Applications Work

WebObjects applications come in two flavors, depending on how much processing you plan to do on the client's computer. Server-based WebObjects applications run entirely on the server, handling HTTP requests and generating HTML pages. Applications that are based on WebObjects' Java Client technology pass objects directly between the server and the client. Although you can construct hybrid applications that use both technologies, for purposes of explanation it's simpler to keep the two technologies separate.

## Server-Based WebObjects Applications

When you run a WebObjects application, it communicates with the web browser through the chain of processes shown in [Figure 4](#apple-ha3demq).

!

Figure 4. Chain of Communication Between the Browser and an HTML-based WebObjects Application

Here is a brief description of these processes:

- __A Web server__. Any HTTP server that uses the Common Gateway Interface (CGI), the Netscape Server API (NSAPI), the Internet Server API (ISAPI), or the Apache API. Although (usually) necessary for deployment, you don't actually need a web server while you develop your WebObjects applications.
- __A WebObjects adaptor__
. A WebObjects adaptor connects WebObjects applications to the web by acting as an intermediary between web applications and HTTP servers.
- __A WebObjects application process__. The application process receives incoming requests and responds to them, usually by returning a dynamically-generated HTML page. You can run multiple instances of this process if one instance is insufficient to handle the application load.

Two of these, WebObjects adaptors and the WebObjects application process, are described in greater detail beginning in [WebObjects Adaptors](WhatIsWebObjects5.md#apple-ha3dgnq).

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects4.md)

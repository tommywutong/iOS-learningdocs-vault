---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/Adaptors.html
archived_at: '2026-07-15T07:52:36.712157Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](RunningWOApp.md)

## WebObjects Adaptors

A WebObjects adaptor receives requests from the server, repackages the requests in a standard format, and forwards them to an appropriate WebObjects application (see [Figure 6](#apple-gqzdsmi)).

!Figure 6. The Role of a WebObjects Adaptor
All WebObjects adaptors communicate with WebObjects applications in the same way, but they communicate with HTTP servers using whatever interface is provided by a particular server. For example, the WebObjects CGI adaptor uses the Common Gateway Interface, the Netscape Interface adaptor uses the Netscape Server API (NSAPI), and the Internet Server adaptor uses the Internet Server API (ISAPI). Thus, WebObjects adaptors can take advantage of server-specific interfaces but still provide server independence.
By default, WebObjects uses the WebObjects CGI adaptor. The Common Gateway Interface is supported by all HTTP servers, so you can use the CGI adaptor with any server-including those that are publicly available. As demands on performance increase, switch to one of the other adaptors with a server that supports the corresponding API (Netscape Server API or Internet Server API). Such servers are capable of dynamically loading the adaptor, eliminating the overhead of starting a new process for each request. As shown in [Figure 7](#apple-g43ds), the communication between the adaptor and the HTTP server occurs inside a single process.

!Figure 7. The Netscape Interface Adaptor
The online document _[Serving WebObjects](../../ServingWebObjects/ServingWebObjectsTOC.md)_ describes how to configure a WebObjects adaptor.

[!Table of Contents](WhatIsWOApp.md) [!Next Section](AppExecutables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

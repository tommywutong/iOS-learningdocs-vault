---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects5.html
archived_at: '2026-07-18T01:20:41.867664Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](WhatIsWebObjects4.md)

## WebObjects Adaptors

An initial request to a WebObjects application consists of a URL like that shown in [Figure 6](#apple-geytmojr).

!

Figure 6. URL to Access a WebObjects Application

When the named server receives the request, it passes the request to the WebObjects adaptor identified in the URL. The adaptor takes the request from the server, repackages it in a standard format, and forwards it to the appropriate WebObjects application (see [Figure 7](#apple-ha3dioa)).

!

Figure 7. The Role of a WebObjects Adaptor

All WebObjects adaptors communicate with WebObjects applications in the same way, but they communicate with HTTP servers using whatever interface is provided by a particular server. For example, the WebObjects CGI adaptor uses the Common Gateway Interface, while the Netscape Interface adaptor uses the Netscape Server API (NSAPI). This allows WebObjects adaptors to take advantage of server-specific interfaces but still provide server independence.
By default, WebObjects uses the WebObjects CGI adaptor. The Common Gateway Interface is supported by all HTTP servers, so you can use the CGI adaptor with any server. As demands on performance increase, you can switch to another adaptor with a server that supports the corresponding API (Netscape Server API, Internet Server API, or Apache API). Such servers are capable of dynamically loading the adaptor and eliminating the overhead of starting a new process for each request.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects6.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-6.html
archived_at: '2026-07-15T08:05:06.865650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](WebObjects%20HTTP%20Adaptors.md) [!](CGI%20Adaptors.md) [!](Installable%20HTTP%20Adaptors.md)

---

# API-based Adaptors

API-based adaptors are WebObjects adaptors based on APIs specific to a particular web server. The NSAPI adaptor, which is based on the Netscape Server 3.5 API, is available on all supported platforms except the Mach-based Mac OS X Server. A WebObjects adaptor based on Microsoft's Internet Information Server API (ISAPI) is also supported on Windows NT. WebObjects supports an adaptor based on Apache's module API on UNIX platforms (including the Mac OS X Server). In addition, Netscape's WAI API is provided as an example project, although is not supported; the WAI adaptor is suitable for all platforms except Mac OS X Server.

The API-based adaptors have a performance advantage over CGI adaptors in that the associated server can dynamically load the adaptor; servers using CGI adaptors, on the other hand, spawn a new adaptor process for each request and kill the process after the response is provided.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](WebObjects%20HTTP%20Adaptors.md) [!](CGI%20Adaptors.md) [!](Installable%20HTTP%20Adaptors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

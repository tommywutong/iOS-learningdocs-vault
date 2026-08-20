---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/InstalledAdaptors.html
archived_at: '2026-07-15T07:55:59.502513Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](AdaptorModes.md)[Previous
Section](AdaptorModes.md) 

## Installed HTTP Adaptors

When WebObjects is installed, the following adaptors
are put in _NeXT_ROOT___/NextLibrary/WOAdaptors__ along with source
code. Note that only the CGI adaptor is installed on Mach, since neither
Netscape's nor Microsoft's servers have been ported to this platform. Also,
no ISAPI binary file is installed on Solaris or HP-UX platforms (only source
code).

The following table summarizes the adaptors provided
with WebObjects.

|  | __Server__ | __NextLibrary Location__ | __Executable__ |
| CGI | many | WOAdaptors/CGI | WebObjects[.exe] |
| NSAPI2 | Netscape 2.0    FastTrack (httpd)    Enterprise (https) | WOAdaptors/NSAPI/2.0 | WebObjects-NSAPI.dll  or  WebObjects-NSAPI.so |
| NSAPI2.0.1 | Netscape 2.0.1    FastTrack (httpd)    Enterprise (https) | WOAdaptors/NSAPI/2.0.1 | WebObjects-NSAPI.dll  or  WebObjects-NSAPI.so |
| NSAPI3 | Netscape 3.0    FastTrack (httpd)    Enterprise (https) | WOAdaptors/NSAPI/2.0 | WebObjects-NSAPI.dll  or  WebObjects-NSAPI.so |
| ISAPI | Microsoft Internet   Information Server    IIS 1.0    IIS 2.0 (NT Server 4.0)    IIS 3.0 (NT Server 4.0)    Peer Web (NT WS 4.0) | WOAdaptors/ISAPI | WebObjects-ISAPI.dll |

```
```

[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](SetUpMonitor.md)[Next
Section](SetUpMonitor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

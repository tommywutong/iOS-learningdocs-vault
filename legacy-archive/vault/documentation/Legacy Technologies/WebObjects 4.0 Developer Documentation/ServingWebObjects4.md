---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects4.html
archived_at: '2026-07-18T01:23:52.948902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects3.md)

## Installable HTTP Adaptors

When WebObjects is installed, the adaptors listed in the table below, when appropriate to the platform, are put in _NEXT_ROOT___/Library/WebObjects/Adaptors__; source code for all adaptors is written to _NEXT_ROOT___/Developer/Examples/WebObjects/Source/WOAdaptors__. Note that only the CGI and Apache adaptors can be found on Mac OS X Server, since neither Netscape's nor Microsoft's servers have been ported to this platform. Also, no ISAPI binary file is written to Solaris or HP-UX platforms (only source code).
The following table summarizes the adaptors provided with WebObjects.

|  |  Server |  /Library/WebObjects/ Location |  Executable |
|  CGI |  many |  Adaptors/CGI |  WebObjects[.exe] |
|  NSAPI |  Netscape 3.51  FastTrack (httpd)  Enterprise (https) |  Adaptors/NSAPI |  WebObjects-NSAPI.dll  or  WebObjects-NSAPI.so |
|  ISAPI |  Microsoft Internet  Information Server  IIS 1.0  IIS 2.0 (NT Server 4.0)  IIS 3.0 (NT Server 4.0)  Peer Web (NT WS 4.0) |  Adaptors/ISAPI |  WebObjects-ISAPI.dll |
|  Apache |  1.3 |  Adaptors/Apache |  mod_WebObjects.o |
|  WAI |  Netscape 3.5 servers |  Adaptors/WAI |  (must build example project) |

```
```


__Note:__  You can find installation instructions for supported HTTP adaptors in _NEXT_ROOT___/Library/WebObjects/Adaptors/InstallationInstructions.html__. The procedure for building HTTP adaptors from provided source code is located in _NEXT_ROOT___/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html__.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](Deploying%20With%20the%20Monitor%20Application.md)

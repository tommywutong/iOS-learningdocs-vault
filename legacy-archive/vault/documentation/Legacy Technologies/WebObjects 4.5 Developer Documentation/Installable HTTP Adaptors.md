---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-7.html
archived_at: '2026-07-15T08:05:07.279274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](WebObjects%20HTTP%20Adaptors.md) [!](API-based%20Adaptors.md) [!](Configuration%20Files.md)

---

# Installable HTTP Adaptors

When WebObjects is installed, the adaptors listed in the table below, when appropriate to the platform, are put in
NEXT_ROOT
__/Library/WebObjects/Adaptors__
; source code for all adaptors is written to  ___NEXT_ROOT___
__/Developer/Examples/WebObjects/Source/Adaptors__
. Note that only the CGI and Apache adaptors can be found on Mac OS X Server, since neither Netscape's nor Microsoft's servers have been ported to this platform. Also, no ISAPI binary file is written to Solaris or HP-UX platforms (only source code).

The following table summarizes the adaptors provided with WebObjects.

| Adaptor | Server | /Library/WebObjects/ Location | Executable |
| --- | --- | --- | --- |
| CGI | many | Adaptors/CGI | WebObjects[.exe] |
| NSAPI | Netscape 3.51   FastTrack (httpd)   Enterprise (https) | Adaptors/NSAPI | WebObjects-NSAPI.dll  or  WebObjects-NSAPI.so |
| ISAPI | Microsoft Internet   Information Server   IIS 1.0   IIS 2.0 (NT Server 4.0)   IIS 3.0 (NT Server 4.0)   Peer Web (NT WS 4.0) | Adaptors/ISAPI | WebObjects-ISAPI.dll |
| Apache | 1.3 | Adaptors/Apache | mod_WebObjects.o |
| WAI | Netscape 3.5 servers | Adaptors/WAI | (must build example project) |

You can find installation instructions for supported HTTP adaptors in  ___NEXT_ROOT___
__/Developer/Examples/WebObjects/Source/Adaptors/InstallationInstructions.html__
. To build HTTP adaptors from provided source code, refer to
NEXT_ROOT
__/Developer/Examples/WebObjects/Source/Adaptors/BuildingInstructions.html__
.

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](WebObjects%20HTTP%20Adaptors.md) [!](API-based%20Adaptors.md) [!](Configuration%20Files.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

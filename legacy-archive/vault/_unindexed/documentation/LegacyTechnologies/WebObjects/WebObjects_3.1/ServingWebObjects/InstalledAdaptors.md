---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/InstalledAdaptors.html
archived_at: '2026-07-15T07:49:56.221460Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](AdaptorModes.md)

# Installed HTTP Adaptors

When WebObjects is installed, the following adaptors are put in _NEXT_ROOT___/NextLibrary/WOAdaptors__ along with source code. Note that only the CGI adaptor is installed on Mach, since neither Netscape's or Microsoft's servers have been ported to this platform. Also, no ISAPI binary file is installed on Solaris or HPUX platforms (only source code).

The following table summarizes the adaptors provided with WebObjects.

|  | Server | NextLibrary Location | Executable |
| --- | --- | --- | --- |
| __CGI__ | many | WOAdaptors/CGI | WebObjects[.exe] |
| __NSAPI__ | _Netscape 1.1_ Communication (httpd)  Commerce (https) | WOAdaptors/NSAPI/1.1 | WebObjects-NSAPI.dll or WebObjects-NSAPI.so |
| __NSAPI2__ | _Netscape 2.0_ FastTrack (httpd) Enterprise (https) | WOAdaptors/NSAPI/2.0 | WebObjects-NSAPI.dll or  WebObjects-NSAPI.so |
| __NSAPI2.0.1__ | _Netscape 2.0.1_ FastTrack (httpd) Enterprise (https) | WOAdaptors/NSAPI/2.0.1 | WebObjects-NSAPI.dll or  WebObjects-NSAPI.so |
| __ISAPI__ | _Microsoft Internet Information Server_  IIS 1.0  IIS 2.0 (NT Server 4.0)  Peer Web (NT WS 4.0) | WOAdaptors/ISAPI | WebObjects-ISAPI.dll |

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](AdminTasks.md)

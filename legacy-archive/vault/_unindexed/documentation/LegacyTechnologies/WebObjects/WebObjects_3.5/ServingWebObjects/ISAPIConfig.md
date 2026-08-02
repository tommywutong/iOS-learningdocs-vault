---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ISAPIConfig.html
archived_at: '2026-07-15T07:55:54.446142Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](NSAPIConfig.md)

## Installing and Configuring the ISAPI Adaptor

If you have one of Microsoft's Internet Information Servers (IIS), such as the Peer Web server that comes with the NT Workstation or the IIS server that comes with NT Server 4.0, you need to install and configure the ISAPI adaptor that comes with WebObjects Enterprise.
__Note__: This procedure is applicable only to the WebObjects Enterprise product on Windows NT platforms.

- Copy the ISAPI adaptor from its installation location to the server's "Scripts" directory:

`cp C:/NeXT/NextLibrary/WOAdaptors/ISAPI/WebObjects-ISAPI.dll C:/INETPUB/Scripts`

This example assumes that _NeXT_ROOT_ is __C:\NeXT\__ and that the IIS server is installed in __C:\INETPUB__. These directories could be different on your system (for instance, the server could be installed in __D:\INETPUB__). This example also shows a copy operation using the __cp__ command in a Bourne shell; alternatively, you could copy the DLL using the NT Explorer program or through similar programs.

- Set up your site so that the proper URL for the ISAPI adaptor is submitted when users click buttons, images, or hyperlinks that have as targets WebObjects applications. This URL has the form:

http://_host_/Scripts/WebObjects-ISAPI.dll/_ApplicationPath_

For HTTP requests that use the CGI adaptor, make sure that the URLs conform to this format:

http://_host_/Scripts/WebObjects.exe/_ApplicationPath_

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](MultipleMonitors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

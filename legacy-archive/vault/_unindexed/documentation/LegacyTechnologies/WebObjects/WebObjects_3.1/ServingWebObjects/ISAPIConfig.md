---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/ISAPIConfig.html
archived_at: '2026-07-15T07:49:55.716863Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](NSAPIConfig.md)

# Installing and Configuring the ISAPI Adaptor

If you have one of Microsoft's Internet Information Servers (IIS), such as the Peer Web server that comes with the NT Workstation or the IIS 2.0 server that comes with NT Server 4.0, you need to install and configure the ISAPI adaptor that comes with WebObjects Enterprise.

__Note__: This procedure is applicable only to the WebObjects Enterprise product on Windows NT platforms.

1. Copy the ISAPI adaptor from its installation location to the server's "Scripts" directory:

   ```
       cp C:/NeXT/NextLibrary/WOAdaptors/ISAPI/WebObjects-ISAPI.dll C:/INETPUB/Scripts
   ```

   This example assumes that _NEXT_ROOT_ is C:\NeXT\ and that the IIS server is installed in C:\INETPUB. These directories could be different on your system (for instance, the server could be installed in D:\INETPUB). This example also shows a copy operation using the __cp__ command in a Bourne shell; alternatively, you could copy the DLL using the NT Explorer program or through similar programs.
2. For load balancing, create a __WebObjects.conf__ file in the NT system directory (usually __C:\WINNT\System32__) or copy an existing __WebObjects.conf__ to that location. Again, the drive letter where Windows NT is installed could be different on your system (it could be "D" instead of "C," for example). See "[Load Balancing](LoadBalancing.md#apple-kjcumnjygyzda)" for the load-balancing procedure.
3. Set up your site so that the proper URL for the ISAPI adaptor is submitted when users click buttons, images, or hyperlinks that have as targets WebObjects applications. This URL has the form:

   ```
       http://host/Scripts/WebObjects-ISAPI.dll/ApplicationPath
   ```

   For HTTP requests that use the CGI adaptor, make sure that the URLs conform to this format:

   ```
       http://host/Scripts/WebObjects.exe/ApplicationPath
   ```

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](Autostarting.md)

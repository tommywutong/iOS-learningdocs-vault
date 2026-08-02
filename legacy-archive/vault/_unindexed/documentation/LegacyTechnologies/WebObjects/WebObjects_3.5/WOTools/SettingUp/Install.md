---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Install.htm
archived_at: '2026-07-15T07:57:42.030205Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](SetUpTOC.md)[Table
of Contents](SetUpTOC.md) [!](Launchng.md)[Previous
Section](Launchng.md) 

## Installing Your Application

Some files in a web application (such as images and
sounds) must be stored under the web server's document root in order for
the server to access them. The remaining files (such as your components
and source code) must be accessible to your application but not necessarily
by the web server itself.

In previous versions of WebObjects, it was
typical to store the entire project under the web server's document root.
This practice has advantages for turnaround time during development. However,
in deployment, it presents the possibility of allowing users access to
your source code. WebObjects 3.5 has a "split installation" feature that
allows you to install only those files (such as images) that the web server
must have access to under the document root. The remaining files can be
stored elsewhere.

The same procedure applies to installing WebObjects
applications and WebObjects frameworks. To install:

1. Click ! to open the Project Inspector. 
2. Under "Install In:", set the path where the application wrapper will be
   installed. This should be _NEXT_ROOT___/NextLibrary/WOApps__ for
   applications and _NEXT_ROOT___/NextLibrary/Frameworks__ for frameworks. 
3. In __Makefile.preamble__ (in the Supporting Files suitcase), set the
   make variable INSTALLDIR_WEBSERVER to the path where your WebObjects applications
   will reside under the document root, usually _DocumentRoot_/__WebObjects__.
   The file contains a line you can uncomment for this purpose. 
4. In Project Builder's Build panel, click !. 
5. From the Target pop-up menu, choose __install__. (By default, the target
   is set to __woapp__.) 
!

6. Click ! in the Build panel to install your
   application. 

The full application wrapper is copied into the "Install In:" directory,
and a wrapper containing only the Web Server Resources is copied into the
document root.

See _[Serving
WebObject](../../ServingWebObjects/ServingWebObjectsTOC.md)_s for more information about installing your application.

[!](SetUpTOC.md)[Table
of Contents](SetUpTOC.md) [!](Convert.md)[Next
Section](Convert.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

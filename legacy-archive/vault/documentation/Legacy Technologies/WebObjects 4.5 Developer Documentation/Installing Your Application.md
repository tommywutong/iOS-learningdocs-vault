---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.18.html
archived_at: '2026-07-15T08:10:07.395276Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Building%20Your%20Application.md) [!](Launching%20Your%20Application.md) [!](Rapid%20Turnaround%20Mode.md)

---

#   Installing Your Application

Some files in a web application (such as images and sounds) must be stored under the web server's document root in order for the server to access them. The remaining files (such as your components and source code) must be accessible to your application but not necessarily by the web server itself.

In previous versions of WebObjects, it was typical to store the entire project under the web server's document root. This practice has advantages for turnaround time during development. However, in deployment, it presents the possibility of allowing users access to your source code. WebObjects has a "split installation" feature that allows you to install only those files (such as images) that the web server must have access to under the document root. The remaining files can be stored elsewhere.

The same procedure applies to installing WebObjects applications and frameworks. To install:

1. 

   Click !
   to open the Project Inspector.
2. 

   Under "Install In:", set the path where the application wrapper will be installed.
3. 

   In Project Builder's Build panel, click !
   .
4. 

   From the Target pop-up menu, choose __install__
   . (By default, the target is set to __woapp__
   .)
   
   !
5. 

   Click !
   in the Build panel to install your application.

   The full application wrapper is copied into the "Install In:" directory, and a wrapper containing only the Web Server Resources is copied into the document root.

See Serving WebObjects for more information about installing your application.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Building%20Your%20Application.md) [!](Launching%20Your%20Application.md) [!](Rapid%20Turnaround%20Mode.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

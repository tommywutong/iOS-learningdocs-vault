---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.16.html
archived_at: '2026-07-15T08:10:05.973280Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Building%20Your%20Application.md) [!](Building%20Your%20Application.md) [!](Launching%20Your%20Application.md)

---

#   The Application Wrapper

When you build your project, Project Builder creates an _application wrapper_
, which is a folder whose name is the project name plus the extension __.woa__
.

!

The application wrapper has a structure similar to that of a framework. It consists of the following:

- 

  The executable application.
- 

  The application's resources.

  These include the application's components as well as other files that are needed by your application at run time.
- 

  The application's web server resources.

When you build and install your application, Project Builder copies all the files from your Web Server Resources suitcase to a folder called WebServerResources inside the application wrapper. If you have client-side Java components in your project, these are also copied to the WebServerResources folder.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Building%20Your%20Application.md) [!](Building%20Your%20Application.md) [!](Launching%20Your%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

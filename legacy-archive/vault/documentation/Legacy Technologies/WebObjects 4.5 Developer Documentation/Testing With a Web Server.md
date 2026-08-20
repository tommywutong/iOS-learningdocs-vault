---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.1b.html
archived_at: '2026-07-15T08:10:08.446388Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Rapid%20Turnaround%20Mode.md) [!](Rapid%20Turnaround%20and%20Direct%20Connect%20Mode.md) [!](Editing%20With%20WebObjects%20Builder.md)

---

#  Testing With a Web Server

When you're working in direct connect mode, few issues arise with respect to rapid turnaround. If your application has features which require a web server be used even for testing, however, there are a couple of things to know to make rapid turnaround work for you. Specifically, since you are relying on the web server to locate files within WebServerResources, you must follow these guidelines:

1. 

   Your projects must reside somewhere below your web server's document root.
2. 

   NSProjectSearchPath should point to all projects of interest.
3. 

   For application projects, the WOApplicationBaseURL user default should specify the directory containing the application project. For example, if your application's project folder is:

   c:\web\docroot\WebObjects\MyApp

   then the WOApplicationBaseURL user default must be "/WebObjects".
4. 

   For framework projects, the WOFrameworksBaseURL user default should specify the directory containing all framework projects used by the application. For example, if your application uses MyFramework.framework and that project resides in:

   c:\web\docroot\WebObjects\Frameworks\MyFramework

   then the WOFrameworksBaseURL user default must be "/WebObjects/Frameworks".

Conveniently, the two examples above use the default locations for WOApplicationBaseURL and WOFrameworksBaseURL; if your projects reside in these default locations, you need only set NSProjectSearchPath.

Also, while it is possible to point WOApplicationBaseURL and WOFrameworksBaseURL to other locations, it is not recommended that WOFrameworksBaseURL be moved since all WebObjects applications use WOExtensions.framework, which resides in the default location. If you set WOFrameworksBaseURL to point elsewhere, one side effect will be that the images in the "Raised Exception" panel will not render.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Rapid%20Turnaround%20Mode.md) [!](Rapid%20Turnaround%20and%20Direct%20Connect%20Mode.md) [!](Editing%20With%20WebObjects%20Builder.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

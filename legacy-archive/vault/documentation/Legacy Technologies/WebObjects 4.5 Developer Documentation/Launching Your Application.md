---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.17.html
archived_at: '2026-07-15T08:10:06.612436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Building%20Your%20Application.md) [!](The%20Application%20Wrapper.md) [!](Installing%20Your%20Application.md)

---

#  Launching Your Application

To launch your application:

1. 

   Click !
   in the toolbar to open the Launch panel.
2. 

   Click !
   in the Launch panel to launch your application.

When you launch your application, your machine's web browser is launched by default and it accesses your application. To turn off this feature:

1. 

   Click !
   to bring up the Launch Options panel.
2. 

   Select Environment and Command-Line Arguments from the pop-up menus.
3. 

   Enter
   -browser OFF
   as a command line option.

You can also launch your application directly from a command line. See Serving WebObjects for more information on command line options.

You can also launch your application by double-clicking its executable file. When you build your application, Project Builder creates an executable file (_ProjectName_
__.exe__
on Windows NT platforms) inside your application wrapper (__.woa__
) directory.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Building%20Your%20Application.md) [!](The%20Application%20Wrapper.md) [!](Installing%20Your%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.3a.html
archived_at: '2026-07-15T08:07:52.010060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Refining%20Main.wo.md) [!](Refining%20Main.wo.md) [!](Specifying%20Default%20Values%20for%20New%20Enterprise%20Objects.md)

---

#   Specifying a Sort Order

You can change your application to sort movies alphabetically without writing any code. Display groups manage sorting behavior, and WebObjects Builder provides a Display Group Options panel for configuring this and other characteristics of display groups.

1. 

   Double-click the __movieDisplayGroup__ variable in the object browser.

   The Display Group Options panel opens for configuring __movieDisplayGroup__.

   !
2. 

   Select the __title__ attribute in the Sorting pop-up list.
3. 

   Select Ascending.
4. 

   Click OK.

WebObjects Builder stores your settings in an archive that specifies how to create and configure __movieDisplayGroup__ at runtime. The archive is stored inside your Main component in a file named __Main.woo__. You can't see the file from Project Builder because you're not meant to edit it directly, but WebObjects Builder's object browser shows you which of your component's variables are initialized from the archive (or __woo__ file) so you don't have to view its contents directly.!

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Refining%20Main.wo.md) [!](Refining%20Main.wo.md) [!](Specifying%20Default%20Values%20for%20New%20Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.e.html
archived_at: '2026-07-15T05:24:02.066743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.d.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.f.md)

---

#   Appearance Manager Memory Requirements

Because appearance design is intended to be very flexible, some appearances may apply complex, nonrectangular shapes to their interface elements. Because data describing these shapes is saved in the form of QuickDraw
Region
structures--which are of variable length, depending upon the complexity of the shapes being described--the amount of memory your application requires may increase when some appearances are active. If your program's 

memory usage is finely tuned according to assumptions about the amount of memory consumed on versions of the Mac OS prior to Mac OS 8.5, and in particular the amount of memory consumed by the Window Manager for each window, you may wish to increase your heap size to accommodate appearance-specific memory usage variations.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.d.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.f.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

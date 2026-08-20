---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.7.html
archived_at: '2026-07-15T05:24:01.165290Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.6.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.8.md)

---

#   Theme-Compliant Cursors

Appearance Manager 1.1 introduces 

cursors that can change appearance with a theme change. In order to be theme-compliant, your program should use these theme-specific cursors whenever possible, instead of the classic black-and-white or color cursors. To obtain theme-compliant cursors, you must use the Appearance Manager to draw cursors in your program, rather than the QuickDraw cursor utilities.

Because the Appearance Manager cursors are color cursors, they currently cannot be set from interrupt time. Therefore, if you support animated cursors that are changed at interrupt time you should continue to use your own cursors for now. The Appearance Manager provides the following functions for specifying theme-compliant cursors:

- 

  `SetThemeCursor`
  sets the cursor to a version of the specified cursor type that is consistent with the current theme.
- 

  `SetAnimatedThemeCursor`
  animates a version of the specified cursor type that is consistent with the current theme.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.6.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.8.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.6.html
archived_at: '2026-07-15T05:24:01.152808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.5.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.7.md)

---

#   Theme-Compliant Sounds

As shown in [Figure 2-6](The%20Appearance%20Control%20Panel.md#apple-gi3tqmby)
, the user can select preferences for the use of 

sounds in a theme. Therefore, not only may users choose to play sounds associated with various aspects of your program's user interface, but the sounds associated with various interface elements may change with a theme change. If you are using standard interface elements (that is, system-defined windows, controls, and menus), the system automatically plays the appropriate sounds, if any, for these elements in the current theme.

Some programs may not use standard interface elements in all instances, however. In such cases, to ensure that your program's sounds match those used in the current theme, you should use the Appearance Manager to determine the sounds that your program uses. The Appearance Manager provides the following functions for playing theme sounds:

- 

  PlayThemeSound
  plays an asynchronous sound associated with the specified state change.
- 

  BeginThemeDragSound
  continuously plays a theme-specific sound associated with the user's movement of a given interface object.
- 

  EndThemeDragSound
  terminates the playing of a sound associated with the user's movement of a given interface object.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.5.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.7.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

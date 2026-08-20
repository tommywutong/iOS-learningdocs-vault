---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.a.html
archived_at: '2026-07-15T05:24:01.203965Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.9.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.b.md)

---

#   Theme-Compliant Menus

Menus allow users to view or choose from a list of choices and commands that your application provides. You can use the Menu Manager to create, display, and manage standard Mac OS menus. To be theme-compliant, your program should either use standard menus or use the Appearance Manager to adapt your custom menu and menu bar elements. For examples and descriptions of standard Mac OS 8._x_
menus, see the _Mac OS 8 Human Interface Guidelines_
at

[http://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html](https://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html)

The Appearance Manager provides the following functions for drawing theme-compliant custom menus:

- 

  DrawThemeMenuBackground
  draws a menu background.
- 

  GetThemeMenuBackgroundRegion
  obtains the background region for a menu.

The Appearance Manager provides the following functions for drawing theme-compliant custom menu titles:

- 

  DrawThemeMenuTitle
  draws a menu title.
- 

  GetThemeMenuTitleExtra
  obtains a measurement of the space to either side of a menu title.

The Appearance Manager provides the following functions for drawing theme-compliant custom menu items:

- 

  DrawThemeMenuItem
  draws a menu item.
- 

  DrawThemeMenuSeparator
  draws a menu item separator line.
- 

  GetThemeMenuItemExtra
  obtains a measurement of the space surrounding a menu item.
- 

  GetThemeMenuSeparatorHeight
  obtains the height of a menu separator line.

The Appearance Manager provides the following functions for drawing theme-compliant custom menu bars:

- 

  DrawThemeMenuBarBackground
  draws a menu bar background.
- 

  GetThemeMenuBarHeight
  obtains the optimal height of a menu bar.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.9.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.b.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

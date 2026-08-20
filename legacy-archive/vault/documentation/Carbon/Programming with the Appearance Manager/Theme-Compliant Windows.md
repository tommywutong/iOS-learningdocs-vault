---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.9.html
archived_at: '2026-07-15T05:24:01.190852Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.8.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.a.md)

---

#   Theme-Compliant Windows

Mac OS applications typically interact with users via 

windows on the screen. You can use the Window Manager to create, display, and manage the drawing and behavior of standard Mac OS windows. Dialog boxes and alert boxes are specific types of windows that are used to present information to and solicit information from the user. You can use the Dialog Manager to readily implement standard Mac OS dialog boxes and alert boxes. To be theme-compliant, your program should either use standard windows or use the Appearance Manager to adapt your custom window, dialog box, and alert box elements. For examples and descriptions of standard Mac OS 8._x_
windows, see the _Mac OS 8 Human Interface Guidelines_
at

[http://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html](https://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html)

The Appearance Manager provides the following functions for applying theme-compliant colors and patterns to custom windows:

- 

  SetThemeWindowBackground
  associates a theme-compliant color or pattern with the background of a window.
- 

  SetThemeTextColorForWindow
  sets a window's foreground color to a theme-compliant color.

The Appearance Manager provides the following functions for drawing theme-compliant custom windows:

- 

  DrawThemeModelessDialogFrame
  draws a beveled outline inside the content area of a modeless dialog box.
- 

  DrawThemeScrollBarDelimiters
  outlines a window's scroll bars.
- 

  DrawThemeStandaloneGrowBox
  draws a size box.
- 

  DrawThemeStandaloneNoGrowBox
  draws a fill image for use in the corner space between scroll bars.
- 

  DrawThemeTitleBarWidget
  draws a close box, zoom box, or collapse box.
- 

  DrawThemeWindowFrame
  draws a window frame.
- 

  DrawThemeWindowHeader
  draws a window header.
- 

  DrawThemeWindowListViewHeader
  draws a window list view header.

The Appearance Manager provides the following functions for obtaining window region information:

- 

  GetThemeStandaloneGrowBoxBounds
  obtains the bounds of a size box.
- 

  GetThemeWindowRegion
  obtains the specified window region.
- 

  GetThemeWindowRegionHit
  obtains the part of the window that the user clicked upon.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.8.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.a.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

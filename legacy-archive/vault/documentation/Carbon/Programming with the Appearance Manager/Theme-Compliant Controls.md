---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.8.html
archived_at: '2026-07-15T05:24:01.177441Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.7.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.9.md)

---

#   Theme-Compliant Controls

Controls are graphical objects, such as buttons, scroll bars, or tabs, that the user can manipulate to take an immediate action or change settings to modify a future action. Your program can use the Control Manager to create standard Mac OS controls. To be theme-compliant, your program should either use standard controls or use the Appearance Manager to adapt its custom control elements. For examples and descriptions of the standard Mac OS 8._x_
controls, see the _Mac OS 8 Human Interface Guidelines_
at

[http://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html](https://developer.apple.com/documentation/mac/HIGOS8Guide/thig-2.html)

Although your program (and the Control Manager) may typically define many different types of 

buttons, for simplicity the Appearance Manager treats various types of buttons--including push buttons, checkboxes, radio buttons, arrow buttons, pop-up menu buttons, disclosure triangles, increment/decrement buttons, and bevel buttons--within a single concept of "buttons." The Appearance Manager provides the following functions for creating theme-compliant custom buttons:

- 

  DrawThemeButton
  draws a button.
- 

  DrawThemePopupArrow
  draws a pop-up arrow.
- 

  GetThemeButtonBackgroundBounds
  obtains the rectangle that contains a button.
- 

  GetThemeButtonContentBounds
  obtains the rectangle where content can be drawn for a button.
- 

  GetThemeButtonRegion
  obtains the region occupied by a button.
- 

  GetThemeCheckBoxStyle
  obtains the system preference for the type of mark to use in a checkbox.

The Appearance Manager also treats various types of rectangular controls--including scroll bars, sliders, and progress bars--as a single concept of "

tracks." The Appearance Manager provides the following functions for creating theme-compliant custom tracks:

- 

  DrawThemeTrack
  draws a track.
- 

  DrawThemeTrackTickMarks
  draws tick marks for a track.
- 

  DrawThemeTickMark
  draws a tick mark.
- 

  DrawThemeScrollBarArrows
  draws scroll bar arrows consistent with the current system preferences.
- 

  GetThemeTrackBounds
  obtains the bounding rectangle of a track.
- 

  GetThemeTrackDragRect
  obtains the area in which the user may drag a track's indicator.
- 

  GetThemeTrackLiveValue
  obtains the current value of a track's indicator, given its relative position.
- 

  GetThemeTrackThumbPositionFromOffset
  obtains the relative position of a track's indicator, given an offset from its prior position.
- 

  GetThemeTrackThumbPositionFromRegion
  obtains the relative position of a track's indicator, given its current position.
- 

  GetThemeTrackThumbRgn
  obtains the region containing a track's indicator.
- 

  GetThemeScrollBarTrackRect
  obtains the area containing the track portion of a scroll bar.
- 

  HitTestThemeTrack
  returns whether the user clicked upon the specified track.
- 

  HitTestThemeScrollBarArrows
  returns whether the user clicked upon the specified scroll bar's arrows.
- 

  GetThemeScrollBarArrowStyle
  obtains the system preference for the type of scroll bar arrows to be used.
- 

  GetThemeScrollBarThumbStyle
  obtains the system preference for the type of scroll box to be used.

The Appearance Manager provides the following functions for creating theme-compliant custom tabs:

- 

  DrawThemeTab
  draws a tab.
- 

  DrawThemeTabPane
  draws a tab pane.
- 

  GetThemeTabRegion
  obtains the region occupied by a tab.

The Appearance Manager provides the following other functions for creating theme-compliant custom controls:

- 

  DrawThemeChasingArrows
  draws an asynchronous arrows indicator.
- 

  DrawThemeEditTextFrame
  draws an editable text frame.
- 

  DrawThemeFocusRect
  draws or erases a focus ring around a specified rectangle.
- 

  DrawThemeFocusRegion
  draws or erases a focus ring around a specified region.
- 

  DrawThemeGenericWell
  draws an image well frame.
- 

  DrawThemeListBoxFrame
  draws a list box frame.
- 

  DrawThemePlacard
  draws a placard.
- 

  DrawThemePrimaryGroup
  draws a primary group box frame.
- 

  DrawThemeSecondaryGroup
  draws a secondary group box frame.
- 

  DrawThemeSeparator
  draws a separator line.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.7.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

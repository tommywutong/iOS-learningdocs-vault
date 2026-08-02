---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.b.html
archived_at: '2026-07-15T05:24:01.216369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.a.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.c.md)

---

#   Theme-Compliant Colors and Patterns

The 

colors used for interface elements may vary from theme to theme. If you are using standard interface elements (that is, system-defined windows, controls, and menus), the colors used for these elements automatically change with a theme change.

Some programs may not use standard interface elements in all instances, however. In such cases, to ensure that your interface elements coordinate with the current theme, you should use the Appearance Manager to determine the colors (and patterns) that your program uses. See [Using Theme-Compliant Colors and Patterns](Using%20Theme-Compliant%20Colors%20and%20Patterns.md#apple-gizdonrz)
for more details on this process.

To be theme-compliant, you should not use any set values for the colors of interface objects in your program. For example, compare the background colors of the two dialog boxes shown in [Figure 2-8](A%20Theme-Compliant%20User%20Interface.md#apple-gmytenzt)
. The non-theme-compliant dialog box uses a set background color of white, which contrasts with the theme-compliant dialog box, whose background color is automatically drawn in gray, the correct color for the current theme.

The Appearance Manager provides the following functions for setting the foreground or background of the current graphics port:

- 

  ApplyThemeBackground
  sets the background color or pattern of the current port to be consistent with that of an embedding object.
- 

  SetThemeBackground
  applies a theme-compliant color or pattern to the background of the current port.
- 

  SetThemePen
  applies a theme-compliant color or pattern to the foreground of the current port.

The Appearance Manager provides the following functions for working with text colors:

- 

  GetThemeTextColor
  obtains the text color used for a specified element under the current theme.
- 

  SetThemeTextColor
  sets the current text color to be consistent with that of a specified element.

The Appearance Manager provides the following functions for obtaining theme color information:

- 

  GetThemeAccentColors
  obtains a copy of a theme's accent colors.
- 

  GetThemeBrushAsColor
  obtains the color that corresponds to a given theme brush type under the current theme.
- 

  IsThemeInColor
  returns whether the current theme would draw in color in the given environment.

The Appearance Manager provides the following functions for working with the drawing state of the current graphics port:

- 

  GetThemeDrawingState
  obtains the drawing state of the current graphics port.
- 

  SetThemeDrawingState
  sets the drawing state of the current graphics port.
- 

  DisposeThemeDrawingState
  releases the memory associated with a reference to a graphics port's drawing state.
- 

  NormalizeThemeDrawingState
  sets the current graphics port to a default drawing state.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.a.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.c.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

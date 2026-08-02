---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.13.html
archived_at: '2026-07-15T05:23:56.450180Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.12.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.14.md)

---

#    Using Theme Brushes

One of the main things that you can do to make your program theme-compliant is to avoid using "fixed" color values for your interface. Instead of hard-coding color values, use the Appearance Manager
ThemeBrush
constants, described in
Theme Brush Constants
, for painting the background of a window or control. Theme brushes are an abstract mechanism that allows colors and patterns to be coordinated with the current theme. A theme brush may specify either an RGB color or a pixel pattern, depending on the theme. You can pass constants of type
ThemeBrush
in the
inBrush
parameter of the functions
SetThemeBackground
,
SetThemePen
, and
SetThemeWindowBackground
to specify that the Appearance Manager substitute whatever the appropriate color or pattern is for a given human interface element in the current theme. Using these brushes makes your existing user interface integrate more smoothly with the current theme.

The
SetThemeBackground
function applies a theme-compliant color or pattern to the background of the current graphics port. Your application should call the
SetThemeBackground
function each time you wish to draw a background in a particular brush type. Note that the
SetThemeBackground
function aligns patterns with local coordinates (0,0) in the current port. To apply a theme-compliant color or pattern to the foreground of the current port, use the
SetThemePen
function. Your application should call the
SetThemePen
function each time you wish to draw a foreground element in a specified brush constant. For use specifically with windows, not ports, the
SetThemeWindowBackground
function sets the theme-compliant color or pattern value to which the Window Manager erases a window's background.

Because
ThemeBrush
constants can represent a color or pattern, depending on the current theme, your application must save and restore the current drawing state of the graphics port around calls to
SetThemeBackground
,
SetThemePen
, and
SetThemeWindowBackground
. For details on this process, see [Saving and Restoring the Drawing Environment](Saving%20and%20Restoring%20the%20Drawing%20Environment.md#apple-gi3dkmrq)
.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.12.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.14.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

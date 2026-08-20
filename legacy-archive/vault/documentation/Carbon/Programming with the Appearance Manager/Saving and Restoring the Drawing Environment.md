---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.15.html
archived_at: '2026-07-15T05:23:56.478499Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.14.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.16.md)

---

#    Saving and Restoring the Drawing Environment

You may have existing code that saves the state of the graphics port before changing the background or pen, and restores the state after drawing. When adopting theme brushes, you should convert your code to use Appearance Manager functions to save and restore all graphics port state values that can be modified by the theme brush, including pixel patterns and other state information that is not typically accessible to applications.

To obtain the current graphics port state values, you can call the function
GetThemeDrawingState
before performing an operation that modifies the drawing state of a graphics port. To return the graphics port to its previous drawing state and release the memory allocated for the drawing state reference, you can call
SetThemeDrawingState
, providing the reference obtained in the
outState
parameter of
GetThemeDrawingState
. You can also call
DisposeThemeDrawingState
to release the allocated memory.

The function
NormalizeThemeDrawingState
sets the current graphics port to a default drawing state.
NormalizeThemeDrawingState
sets the background of a graphics port to white; the pen of the port to a size of 1 pixel by 1 pixel, a pattern mode of
patCopy
, and a pattern of black; and the text mode of the port to
srcOr
. The
NormalizeThemeDrawingState
function also flushes from memory any color foreground or background patterns saved in the port's
GrafPort.pnPat
or
GrafPort.bkPat
fields, respectively.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.14.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.16.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

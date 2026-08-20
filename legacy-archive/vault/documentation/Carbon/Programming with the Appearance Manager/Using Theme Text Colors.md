---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.14.html
archived_at: '2026-07-15T05:23:56.465104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.13.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.15.md)

---

#    Using Theme Text Colors

The Appearance Manager also provides a wide variety of text colors for drawing the text of a control. Again, instead of hard-coding color values for text, use the Appearance Manager's
ThemeTextColor
constants, described in
Theme Text Color Constants
, which identify a particular context in which text is used. You can pass a constant of type
ThemeTextColor
to the function
SetThemeTextColor
to specify that the Appearance Manager substitute whatever the appropriate text color is for a given context under the current theme. You can use the function
GetThemeTextColor
to obtain the actual color in use under the current theme for the specified
ThemeTextColor
constant. When you use the
ThemeTextColor
constants in your program, the Appearance Manager automatically applies the correct color for text in the current theme.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.12.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.13.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.15.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.5.html
archived_at: '2026-07-15T05:24:00.569316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.4.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.6.md)

---

#   Theme-Compliant Fonts

As shown in [Figure 2-9](#apple-giydgnbr)
, the user can use the Appearance control panel to select the preferences for the system 

fonts in a theme. Because of this, system fonts may change with a theme change while your program is running. If you are using standard interface elements (that is, system-defined windows, controls, and menus), the fonts used for these elements automatically change with a theme change.

Some programs may not use standard interface elements in all instances, however. For example, a program may draw its own text into a dialog box. In such cases, to ensure that the fonts you use match the corresponding system fonts in the current theme, you should use the Appearance Manager to determine the fonts that you use. The Appearance Manager provides the following functions for working with theme fonts:

__Figure 2-9__  

Examples of the views font, the large system font, and the small system font

!

- 

  GetThemeFont
  obtains information about a system font in the current theme.
- 

  UseThemeFont
  sets the font of the current graphics port to one of the current theme's system fonts.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.4.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.4.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.6.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.4.html
archived_at: '2026-07-15T05:23:59.973425Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.3.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.5.md)

---

#   A Theme-Compliant User Interface

A 

theme-compliant program is either one that uses only standard Mac OS human interface elements (that is, controls, windows, and other elements created from standard definition functions) or one that contains custom interface elements but uses the Appearance Manager to be theme-compliant.

Theme-compliant interface elements automatically coordinate with the rest of the user interface under any theme. An interface element that is not theme-compliant may appear to be visually incongruous or may not provide the same behavior (such as not having smart scrolling features) as a theme-compliant element.

[Figure 2-8](#apple-gmytenzt)
shows the same dialog box, before and after being made theme-compliant. Comparing the two dialog boxes, you can see that the theme-compliant version uses the correct background color (gray) for the platinum appearance. Another difference is that the theme-compliant dialog box uses standard system-defined primary group boxes; these group boxes have a beveled look in the platinum appearance and allow you to use a checkbox item for the title of the group box. Finally, the theme-compliant dialog box also makes use of a standard focus ring for the editable text field into which the user may currently type.

__Figure 2-8__  

The same dialog box, before and after being made theme-compliant

!

The key to making your program theme-compliant is to allow the system to do as much of your interface work for you as is possible. Using the standard, system-defined interface elements is the biggest step you can take toward theme-compliance. However, if your program uses custom interface elements, you must then use the Appearance Manager to adapt these nonstandard elements to the same coordinated look as the rest of the Mac OS. See [Case Studies for Making Custom Interface Elements Theme-Compliant](Case%20Studies%20for%20Making%20Custom%20Interface%20Elements%20Theme-Compliant.md#apple-ge4tkmrr)
for examples of making various custom control elements theme-compliant.

Of course, the specific actions necessary to achieve theme-compliance vary from program to program, so you should use the checklist provided in [A Checklist for Creating a Theme-Compliant Program](A%20Checklist%20for%20Creating%20a%20Theme-Compliant%20Program.md#apple-geztgnrr)
to determine what you need to do to make your program theme-compliant.

The following sections discuss the elements of a theme-compliant user interface in more detail:

- 

  [Theme-Compliant Fonts](Theme-Compliant%20Fonts.md#apple-ge3tkmbr)
- 

  [Theme-Compliant Sounds](Theme-Compliant%20Sounds.md#apple-gqydoojy)
- 

  [Theme-Compliant Cursors](Theme-Compliant%20Cursors.md#apple-giydsmzq)
- 

  [Theme-Compliant Controls](Theme-Compliant%20Controls.md#apple-geytgnzw)
- 

  [Theme-Compliant Windows](Theme-Compliant%20Windows.md#apple-ge2diobu)
- 

  [Theme-Compliant Menus](Theme-Compliant%20Menus.md#apple-gm4damjq)
- 

  [Theme-Compliant Colors and Patterns](Theme-Compliant%20Colors%20and%20Patterns.md#apple-gqytqnzy)

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.3.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

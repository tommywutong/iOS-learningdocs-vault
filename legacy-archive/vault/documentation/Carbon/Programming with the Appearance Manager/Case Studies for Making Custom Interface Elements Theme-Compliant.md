---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.17.html
archived_at: '2026-07-15T05:23:56.506056Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.16.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.18.md)

---

#    Case Studies for Making Custom Interface Elements Theme-Compliant

As discussed in [A Checklist for Creating a Theme-Compliant Program](A%20Checklist%20for%20Creating%20a%20Theme-Compliant%20Program.md#apple-geztgnrr)
, the easiest way to have your program's interface be theme-compliant is to use the system-defined menus, windows, and controls rather than creating your own. For example, the Mac OS 8 Control Manager supports a variety of new control definitions, as well as enhancements to existing controls, all of which are completely theme-compliant. In the case of your program's controls, if you find that you cannot use the system definitions supplied by Control Manager for all your needs, you then should use the Appearance Manager to ensure that those custom control elements in your program are theme-compliant.

The following four "before and after" case studies show how you can use the Appearance Manager to make a custom control element theme-compliant. Each case presents both a non-theme-compliant, custom control element (in our examples, a frame for an editable text field) and the theme-compliant version of the same element. The cases differ in the ways in which the non-theme-compliant elements have originally been implemented, which, in turn, affects how one makes the elements theme-compliant with the Appearance Manager. You may note that--even in these simple examples--in each case drawing the element with the Appearance Manager requires even less code than is needed for the original, non-theme-compliant drawing.

- 

  [Making an Object Drawn With QuickDraw Theme-Compliant](Making%20an%20Object%20Drawn%20With%20QuickDraw%20Theme-Compliant.md#apple-gmytknbu)
- 

  [Making a Dialog User Item Theme-Compliant](Making%20a%20Dialog%20User%20Item%20Theme-Compliant.md#apple-gqydamrs)
- 

  [Making a Control User Pane Theme-Compliant](Making%20a%20Control%20User%20Pane%20Theme-Compliant.md#apple-gi2tmoby)
- 

  [Making a Custom Definition Function Theme-Compliant](Making%20a%20Custom%20Definition%20Function%20Theme-Compliant.md#apple-ge2dcmjw)

For a discussion of drawing theme-compliant tracks in your program, see [Drawing Tracks](Drawing%20Tracks.md#apple-gmytcnrv)
.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.16.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.18.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

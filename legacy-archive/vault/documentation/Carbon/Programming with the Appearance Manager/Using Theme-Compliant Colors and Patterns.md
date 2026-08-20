---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.12.html
archived_at: '2026-07-15T05:23:56.437711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.11.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.13.md)

---

#    Using Theme-Compliant Colors and Patterns

As mentioned in [A Checklist for Creating a Theme-Compliant Program](A%20Checklist%20for%20Creating%20a%20Theme-Compliant%20Program.md#apple-geztgnrr)
, one of the first steps in becoming theme-compliant is to remove color table resources for windows, controls, menus, dialog boxes, and alert boxes from your program. The system no longer fully supports the
'wctb'
,
'ictb'
,
'mctb'
,
'dctb'
,
'actb'
, and
'cctb'
resources, which typically have been used to specify custom color information for interface elements. In some cases, using these resources can inhibit the ability of your user interface to integrate with the current theme. For theme-compliant dialog boxes and alert boxes, instead use the following Mac OS 8 Dialog Manager resources: the dialog font table resource (
'dftb'
), the extended dialog resource (
'dlgx'
), and the extended alert resource (
'alrx'
).

Other steps you can take to ensure that your program's use of color is theme-compliant are described in the following sections:

- 

  [Using Theme Brushes](Using%20Theme%20Brushes.md#apple-ge2dimbz)
- 

  [Using Theme Text Colors](Using%20Theme%20Text%20Colors.md#apple-gmzdgnrq)
- 

  [Saving and Restoring the Drawing Environment](Saving%20and%20Restoring%20the%20Drawing%20Environment.md#apple-gi3dkmrq)
- 

  [Obtaining Device Color and Depth Information](Obtaining%20Device%20Color%20and%20Depth%20Information.md#apple-gmztknzy)

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.11.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.13.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

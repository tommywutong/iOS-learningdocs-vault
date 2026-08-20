---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.10.html
archived_at: '2026-07-15T05:23:55.426619Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)


__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.f.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.11.md)

---

#   A  Checklist for Creating a Theme-Compliant Program

The key to making your program theme-compliant is to allow the system to do as much of your interface work for you as possible. Using the standard, system-defined interface elements is one major step toward theme-compliance. Avoiding making hard-coded assumptions about dimensions and colors is another major step. Both steps save you engineering effort and repay you with a theme-compliant interface. The specific actions necessary to achieve theme-compliance vary from program to program, so you should use the 

checklist below to determine what you need to do to make your program theme-compliant.

- 

  Register with the Appearance Manager. See [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
  for more details.
- 

  Whenever possible, use the system-defined windows supplied by the Window Manager instead of creating your own. With Mac OS 8.5 and 8.6, the Window Manager provides extensive support for a variety of window features, including floating windows, that developers previously had to implement on their own.
- 

  Whenever possible, use the system-defined menus provided by the Menu Manager instead of creating your own. With Mac OS 8 and 8.5, the Menu Manager supports a variety of long-requested features, including: an extended selection of available modifier keys to use for keyboard equivalents, different fonts for individual menu items, a wider selection of icon data formats, and menu item command IDs.
- 

  Whenever possible, use the wide assortment of system-defined controls available with the Mac OS 8 Control Manager instead of creating your own. At a minimum, you should revise any custom controls in your program so that they work in control hierarchies.
- 

  Make your dialog boxes and alert boxes theme-compliant. The Mac OS 8 Dialog Manager introduces two new resources--the
  'dlgx'
  and
  'alrx'
  resources--that you can use to specify theme-compliant features for your dialog boxes and alert boxes, respectively.
- 

  Where you absolutely cannot use standard interface elements, use Appearance Manager functions to adapt your custom elements to a theme-compliant look. See [Case Studies for Making Custom Interface Elements Theme-Compliant](Case%20Studies%20for%20Making%20Custom%20Interface%20Elements%20Theme-Compliant.md#apple-ge4tkmrr)
  for some examples of using the Appearance Manager to make custom control elements theme-compliant.
- 

  Remove color table resources for windows, controls, menus, dialog boxes, and alert boxes from your program. Because they limit theme-compliance, these resources--typically used to specify custom color information for interface elements--are now mostly ignored by the system.
- 

  Make no assumptions about color values for your interface. Instead of hard-coding color values, use the Appearance Manager's
  ThemeBrush
  and
  ThemeTextColor
  constants, described in
  Theme Brush Constants
  and
  Theme Text Color Constants
  . When you use these constants in your program, the Appearance Manager automatically applies the correct color or pattern for a given interface element in the current theme. See [Using Theme-Compliant Colors and Patterns](Using%20Theme-Compliant%20Colors%20and%20Patterns.md#apple-gizdonrz)
  for more details on handling color in your program's interface.
- 

  Because the measurements of standard interface objects may change in a given appearance, you should make no assumptions about the dimensions of menus, windows, or controls. For example, relying on an unchanging menu bar height in order to position your windows means that you could end up with the menu bar overlapping your windows after a theme change. Instead of relying on hard-coded dimension values, you should call Appearance Manager functions to obtain the measurements that are used in the current theme.
- 

  Call Appearance Manager functions to use theme-compliant color cursors in your program.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.f.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.11.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.f.html
archived_at: '2026-07-15T05:24:02.078164Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.1.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.e.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.10.md)

---

#   Using the Appearance Manager

Many programs exclusively use standard, system-defined interface elements. If yours is one of these, you may only need to register your program with the Appearance Manager and be prepared to respond to Appearance Manager Apple events in order to be theme-compliant. However, if your program uses any custom interface elements, you may need to use other features of the Appearance Manager for your program to be theme-compliant.

This chapter discusses how you can use the Appearance Manager, through version 1.1, in the following sections:

- 

  [A Checklist for Creating a Theme-Compliant Program](A%20Checklist%20for%20Creating%20a%20Theme-Compliant%20Program.md#apple-geztgnrr)
  presents the main steps you should take to make your program theme-compliant.
- 

  [Becoming a Client of the Appearance Manager](Becoming%20a%20Client%20of%20the%20Appearance%20Manager.md#apple-gqydmnrt)
  describes the process of checking for and registering with the Appearance Manager.
- 

  [Using Theme-Compliant Colors and Patterns](Using%20Theme-Compliant%20Colors%20and%20Patterns.md#apple-gizdonrz)
  discusses how to work with color in your interface.
- 

  [Case Studies for Making Custom Interface Elements Theme-Compliant](Case%20Studies%20for%20Making%20Custom%20Interface%20Elements%20Theme-Compliant.md#apple-ge4tkmrr)
  presents examples of making custom interface elements theme-compliant.
- 

  [Creating Custom Themes](Creating%20Custom%20Themes.md#apple-gmydenjz)
  describes how to set up a custom environment for your program.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.1.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.e.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

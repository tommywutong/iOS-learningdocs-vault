---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.1.html
archived_at: '2026-07-15T05:23:55.156920Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)


__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Next](attachments/Concepts/images/next.gif)](Appearance.2.md)

---

#  Introduction

This document describes how your program can use the Appearance Manager, through Appearance Manager version 1.1.

The Appearance Manager coordinates the look of human interface elements on the Mac OS and provides the underlying support for appearances and themes. __Appearances__
unify the look of human interface elements in your program and across the system--including alert icons, controls, background colors, dialog boxes, menus, windows, and state transitions--thus giving the user a consistent experience. __Themes__
bundle additional user preferences regarding such interface aspects as sounds, desktop pictures or patterns, and system fonts.

You can use the Appearance Manager to adapt any nonstandard interface elements in your program to the same coordinated look as the rest of the Mac OS. The Appearance Manager also provides many standard human interface elements, such as focus rings and group boxes, that can eliminate the need to create and maintain your own custom solutions.

Many programs exclusively use standard, system-defined interface elements. If yours is one of these, you may need only to register your program with the Appearance Manager and be prepared to respond to Appearance Manager Apple events in order to coordinate with the systemwide look, that is, to be __theme-compliant__
. However, if your program uses any custom interface elements, you may need to use other features of the Appearance Manager for your program to be theme-compliant.

If your program has a user interface, you should read this document to learn how to give your program a look consistent with the system and other Mac OS programs. Documentation on related Mac OS human interface technologies is available at

[http://developer.apple.com/documentation/macos8/mac8.html](https://developer.apple.com/documentation/macos8/mac8.html)

The following chapters describe the Appearance Manager:

-   [About the Appearance Manager](About%20the%20Appearance%20Manager.md#apple-gmydemzx) introduces the Appearance Manager and its
  capabilities.
-   [Using the Appearance Manager](Using%20the%20Appearance%20Manager.md#apple-gmydemzx) provides examples of how your program can
  use the Appearance Manager.
-   [Document Version History](Document%20Version%20History.md#apple-giztmmzv) provides a history of corrections and other changes
  to this document.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Next](attachments/Concepts/images/next.gif)](Appearance.2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

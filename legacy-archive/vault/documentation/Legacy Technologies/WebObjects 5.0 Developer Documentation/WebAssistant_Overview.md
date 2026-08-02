---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/WebAssistant_Overview.html
archived_at: '2026-07-15T08:12:41.565192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Running_the_ppletviewer.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Restricting_to_Entities.md)

## WebAssistant Overview

When the Web Assistant applet is launched, it appears in a
window whose title indicates the current page and entity:

![[image: ../Art/wapropertieslist.gif]](../Art/wapropertieslist.gif)

The WebAssistant has four displays, each selectable by clicking
a tab:

- __Properties__ Allows
  you to set which properties of an entity are shown in a page, the order
  in which they're displayed, and the display characteristics of
  properties (for example, color and alignment).
- __Page__ Allows you to customize global
  page properties, such as template, overall style, color, and border
  thickness.
- __Generation__ Only available in expert
  mode, this display allows you to generate templates and "freeze"
  customized pages as reusable components.
- __Entities__ Allows you to select which
  entities of the model are hidden, which are shown, and which are
  read-only.

The WebAssistant stays synchronous with your browser. When
you navigate to a new page, it displays the settings for that page.

The Web Assistant has two modes, Standard mode and Expert
mode. By default the Web Assistant opens in Standard mode, which
lets you customize the current page in your application. When you
customize a page in Standard mode, the changes apply to all occurrences
of that page, and that page only. For example, if you change the
order of properties in an edit page for the Movie entity, then any
time a Movie edit page is displayed, those changes are in effect
(provided you have clicked Update or Save). However, the changes
don't apply to a Movie query, list, or inspect page; if you want
to customize those in the same way, you must do so explicitly.

Using Web Assistant's Expert mode, you can customize any
page in the application, regardless of whether it is currently displayed.
Thus, by specifying the "\*all\*" setting in Expert mode, you
could change all pages of a given entity at once. In addition, you
can generate a template or "freeze" a page as a reusable component.
For more information, see ["WebAssistant Expert Mode"](WebAssistant_Expert_Mode.md#apple-ijbusssdircei).

When you've made changes to a page, you can use the buttons
at the bottom of the WebAssistant to apply them:

- __Update__ sends
  your changes to the server. On some systems this causes the page
  to be refreshed in your browser.
- __Revert__ causes all settings to revert
  to their last saved values.
- __Use Defaults__ reverts all settings to
  the values they had when the project was created.
- __Save__ saves the changes to disk. You
  need to save your changes in order for them to persist beyond the
  current session.

The _Info_ button displays a brief description
of the currently selected Direct to Web component.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Running_the_ppletviewer.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Restricting_to_Entities.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

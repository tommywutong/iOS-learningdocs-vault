---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Setting_Whi_e_Displayed.html
archived_at: '2026-07-15T08:12:31.108590Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_Pages.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Changing_Ho_e_Displayed.md)

## Setting Which Properties are Displayed

The Properties display of the WebAssistant enables you to
specify which properties of an entity appear in a page (or component)
and the order in which these properties appear. Most of the user-interface
elements for accomplishing these things are in the left half of
the display as shown in the following example:

![[image: ../Art/wapropertieslistexplained.gif]](../Art/wapropertieslistexplained.gif)

The entity's properties (attributes and relationships) in
the Show column are displayed in the page. To the left of the arrows
is a key browser that shows relationships (which appear with a "+")
and hidden attributes. You can click on a relationship to show its
attributes and relationships in the next column of the key browser.

The WebAssistant displays the keys that can be found in the
entity's source code. If you want to show a key or key path that
doesn't appear, you can type in the text field.

For each property, you can

- Move it to
  the key browser by selecting it and clicking the left arrow. This
  hides the property. Similarly, if a property is hidden, you can
  show it by selecting it and clicking the right arrow.
- Move it up or down in the list by clicking the up and down
  arrows. This changes the order of appearance of the properties in
  the page (left to right or top to bottom, depending on the component).

By default, the WebAssistant shows only class properties.
If you want to show a custom method or a keypath, click the Add
button. A dialog box is displayed in which you can enter your custom
key or key path (for example, "studio.budget").

You can also change the title for a property by editing the
string in the Display (Disp.) field. This change only affects the
way the property is labeled in the page, and has no effect on the
actual property name.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Customizing_Pages.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Changing_Ho_e_Displayed.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

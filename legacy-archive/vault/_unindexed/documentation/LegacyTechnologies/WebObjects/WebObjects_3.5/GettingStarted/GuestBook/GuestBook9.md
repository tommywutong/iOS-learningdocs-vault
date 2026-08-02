---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook9.html
archived_at: '2026-07-15T07:53:37.688025Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook8.md)

## Resizing the Form Elements

The text fields and text area are a bit small, so you'll resize them using the Inspector window.
To inspect an element, you must first select it. Some elements (such as text fields and text areas) can be selected simply by clicking them; they appear with a gray line underneath.
!
You select text elements as you would in most text-editing applications (by dragging, or by double-clicking words, or by triple-clicking lines); they appear with gray shading.

- Inspect the Name text field (that is, select the text field and open the Inspector window).
  !
- Change the setting of the pop-up list at the upper right of the window from Dynamic Inspector to Static Inspector.

All WebObjects elements have a _dynamic inspector_, that is, one that allows you to set bindings (you'll work with bindings in the next section). In addition, many WebObjects elements (those with direct counterparts in static HTML) also have a _static inspector__._ This inspector allows you to set the standard HTML attributes for that type of element.

In this window, you can set various attributes of the static counterpart of a WOTextField, which is an HTML <INPUT TYPE=TEXT> element.

- In the Size field, type 20 and press Enter to set the width of the text field to 20 characters.

__Note:__ Be sure to press Enter after typing the values; otherwise, they won't "stick."

- Repeat steps 1 through 3 for the E-mail field.
- Inspect the multi-line text area.

In Text Area Inspector, you can set various attributes corresponding to those of a <TEXTAREA> element.

- Increase the size of the element by specifying the number of columns and number of rows to, say, 30 and 6.
- Save the Main component.

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook10.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.e.html
archived_at: '2026-07-15T08:08:43.202981Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20the%20Page%27s%20Content.md) [!](Creating%20Form-Based%20Dynamic%20HTML%20Elements.md) [!](Binding%20Elements.md)

---

#  Resizing the Form Elements

The text fields and text area are a bit small, so you'll resize them using the Inspector panel.

To inspect an element, you must first select it. Some elements (such as text fields and text areas) can be selected simply by clicking them; they appear shaded.

You select text elements as you would in most text-editing applications (by dragging, or by double-clicking words, or by triple-clicking lines); they appear highlighted when selected.

1. 

   Select the Name text field.
2. 

   In the Textfield Inspector, change the setting of the pop-up list at the upper left of the panel from Dynamic Inspector to Static Inspector.

!

All WebObjects elements have a _dynamic inspector,_ that is, one that allows you to set bindings (you'll work with bindings in the next section). In addition, many WebObjects elements (those with direct counterparts in static HTML) also have a _static inspector_. This inspector allows you to set the standard HTML attributes for that type of element.

In this panel, you can set various attributes of the static counterpart of a WOTextField, which is an HTML <INPUT TYPE=TEXT> element.

- 

  In the Visible length field, enter 20 to set the width of the text field to 20 characters.
- 

  Repeat steps 1 through 3 for the E-mail field.
- 

  Select the multi-line text area.

  In the Text Area Inspector, you can set various attributes corresponding to those of a <TEXTAREA> element.
- 

  Increase the size of the element by specifying the number of columns and number of rows to, say, 30 and 6.
- 

  Save the Main component.

  ---

  © 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

  [!](Creating%20the%20Page%27s%20Content.md) [!](Creating%20Form-Based%20Dynamic%20HTML%20Elements.md) [!](Binding%20Elements.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)

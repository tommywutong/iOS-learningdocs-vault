---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.24.html
archived_at: '2026-07-15T08:10:16.277018Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20WebObjects%20Builder%20Toolbar.md) [!](Entering%20Text.md) [!](Menu%20Equivalents%20For%20Toolbar%20Commands.md)

---

#  Creating Elements With the Toolbar

To create HTML elements, you use the buttons in the toolbar. There are three groups of buttons.

- 

  __Structures__ !
  .
  Use these buttons to create paragraphs, lists, images, and other static HTML elements. See [Structure Elements](Structure%20Elements.md#apple-gm3dsobv)
  for more information.
- 

  __Dynamic form elements__ !
  .
  Use these buttons to create form elements in which users enter information. WebObjects gives your application access to the data entered by users by allowing you to associate, or _bind_
  , these elements to variables in your application. See [Creating Form-Based Dynamic Elements](Creating%20Form-Based%20Dynamic%20Elements.md#apple-he3tsmbs)
  for more information.
- 

  __Other WebObjects__ !
  .
  Use these buttons to create other dynamic elements, which you can bind to variables and methods in your program to control how they are displayed. Some of these (such as hyperlinks) have direct HTML equivalents. Others are _abstract dynamic elements_
  , such as repetitions and conditionals, which determine how many times an element is displayed or whether it is displayed at all. See [Creating Other WebObjects](Creating%20Other%20WebObjects.md#apple-gqydsnzs)
  for detailed information.

The general procedure for creating an HTML element is:

1. 

   Place the cursor where you want the element to appear on the page.
2. 

   Click the toolbar button representing the element you want.

   The element is placed at the cursor position.
3. 

   Select the element (see [Selecting Elements in the Layout and Preview Views](Selecting%20Elements%20in%20the%20Layout%20and%20Preview%20Views.md#apple-giztambr)
   ). In most cases, the element is already selected when you create it.
4. 

   Bring the Inspector to the front by clicking it. If it is not open, click !
   .

   In the Inspector, you can set various properties of the element. For example, you can change a paragraph's type from plain to preformatted.

It's important to be aware of what happens when you have text or other elements selected and you create a new element:

- 

  If the new element is a _container_
  element (that is, it can contain other elements), the selected elements are "wrapped" or contained inside the new element.
- 

  If the new element cannot contain other elements (for example, a horizontal rule or image), the new element replaces the selection.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20WebObjects%20Builder%20Toolbar.md) [!](Entering%20Text.md) [!](Menu%20Equivalents%20For%20Toolbar%20Commands.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

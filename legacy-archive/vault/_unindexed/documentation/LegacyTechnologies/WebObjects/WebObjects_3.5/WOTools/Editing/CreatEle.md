---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/CreatEle.htm
archived_at: '2026-07-15T07:56:50.997996Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](EntText.md)[Previous
Section](EntText.md) 

## Creating Elements With the Toolbar

To create HTML elements, you use the buttons on the
bottom row of the toolbar (or at the right of the toolbar if your window
is large). There are four groups of buttons, only one of which is displayed
at a time. The pop-up list ! lets you switch
the group of buttons that are displayed to its right. The groups are:

- __Structures !.__ Use these buttons to create
  paragraphs, lists, images, and other static HTML elements. See ["Structure
  Elements"](StrucEle.md#apple-g43dkoa) for more information. 
- __Tables !.__ Use these buttons to create
  and manipulate HTML table elements. See ["Working
  With Tables"](WrkTabls.md#apple-geydimjq) for more information. 
- __Dynamic form elements !.__ Use these buttons
  to create form elements in which users enter information. WebObjects gives
  your application access to the data entered by users by allowing you to
  associate, or _bind_, these elements to variables in your application.
  See ["Creating Form-Based Dynamic Elements"](../DynamicElements/FormBase.md#apple-gy2danq)
  for more information. 
- __Other WebObjects !.__ Use these buttons
  to create other dynamic elements, which you can bind to variables and methods
  in your program to control how they are displayed. Some of these (such
  as hyperlinks) have direct HTML equivalents. Others are _abstract dynamic
  elements_, such as repetitions and conditionals, which determine how
  many times an element is displayed or whether it is displayed at all. See
  ["Creating Other WebObjects"](../DynamicElements/CreateWO.md#apple-guydooi) for detailed
  information.

The general procedure for creating an HTML element is:

1. Place the cursor where you want the element to appear on the page. 
2. Click the toolbar button representing the element you want. 

The element is placed at the cursor position.

3. Select the element (see ["Selecting Elements"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/SelElemhtm#7524)).
   In most cases, the element is already selected when you create it. 
4. Bring the Inspector to the front by clicking it. If it is not open, click !. 

In the Inspector, you can set various properties of the element. For
example, you can change a paragraph's type from plain to preformatted.

It's useful to be aware of what happens when you have
text or other elements selected and you create a new element:

- If the new element is a _container_ element (that is, it can contain
  other elements), the selected elements are "wrapped" or contained inside
  the new element. 
- If the new element cannot contain other elements (for example, a horizontal
  rule or image), the new element replaces the selection.

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](MenuEqv.md)[Next
Section](MenuEqv.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

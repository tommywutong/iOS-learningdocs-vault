---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing6.html
archived_at: '2026-07-18T01:27:26.205114Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Editing5.md)

## Creating Elements With the Toolbar

To create HTML elements, you use the buttons on the bottom row of the toolbar (or at the right of the toolbar if your window is large). There are four groups of buttons, only one of which is displayed at a time. The pop-up list ! lets you switch the group of buttons that are displayed to its right. The groups are:

- __Structures__ !__.__ Use these buttons to create paragraphs, lists, images, and other static HTML elements. See ["Structure Elements"](Structure%20Elements.md#apple-g43dkoa) for more information.
- __Tables__ !__.__ Use these buttons to create and manipulate HTML table elements. See ["Working With Tables"](Working%20With%20Tables.md#apple-geydimjq) for more information.
- __Dynamic form elements__ !__.__ Use these buttons to create form elements in which users enter information. WebObjects gives your application access to the data entered by users by allowing you to associate, or _bind_, these elements to variables in your application. See ["Creating Form-Based Dynamic Elements"](Creating%20Form-Based%20Dynamic%20Elements.md#apple-gy2danq) for more information.
- __Other WebObjects__ !__.__ Use these buttons to create other dynamic elements, which you can bind to variables and methods in your program to control how they are displayed. Some of these (such as hyperlinks) have direct HTML equivalents. Others are _abstract dynamic elements_, such as repetitions and conditionals, which determine how many times an element is displayed or whether it is displayed at all. See ["Creating Other WebObjects"](Creating%20Other%20WebObjects.md#apple-guydooi) for detailed information.

The general procedure for creating an HTML element is:

- Place the cursor where you want the element to appear on the page.
- Click the toolbar button representing the element you want.

The element is placed at the cursor position.

- Select the element (see ["Selecting Elements"](Editing8.md#apple-g42tena)). In most cases, the element is already selected when you create it.
- Bring the Inspector to the front by clicking it. If it is not open, click !.

In the Inspector, you can set various properties of the element. For example, you can change a paragraph's type from plain to preformatted.

It's important to be aware of what happens when you have text or other elements selected and you create a new element:

- If the new element is a _container_ element (that is, it can contain other elements), the selected elements are "wrapped" or contained inside the new element.
- If the new element cannot contain other elements (for example, a horizontal rule or image), the new element replaces the selection.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Editing7.md)

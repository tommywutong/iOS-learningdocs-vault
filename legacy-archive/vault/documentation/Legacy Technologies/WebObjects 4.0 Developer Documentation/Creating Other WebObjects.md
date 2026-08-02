---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements12.html
archived_at: '2026-07-18T01:25:36.375943Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Dynamic%20and%20Static%20Inspectors.md)

# Creating Other WebObjects

!

You use this toolbar to create all dynamic elements other than form-based elements. This section provides some general information about using these elements. Each element is described in more detail in its own section.
To create a dynamic element, you click its toolbar icon. One thing to be aware of is what happens when there are already elements selected when you create the element:

- Some dynamic elements (WOHyperlink, WOConditional, WORepetition, custom WebObjects and generic WebObjects) can contain other elements. In this case, the selected elements appear with the new element "wrapped" around it.
- Other dynamic elements (WOString, WOImage, WOActiveImage, and WOApplet) can't contain other elements. When you create one, it replaces whatever was selected.

The first six dynamic element types (all those except for WOImage, WOActiveImage, and WOApplet) display with a pair of icons surrounding the element (and possibly other icons in between). For example, when you create a repetition, it appears like this in the component window:

!

To bind a dynamic element, you drag from an item in the object browser to one of the outer icons. The Inspector appears, allowing you to complete the binding. See ["Binding Elements"](Binding%20Elements-2.md#apple-gy2tioi) for more information.

You can double-click one of the icons to collapse the element into a single icon:
!
Collapsing can be desirable when you have dynamic elements that contain other elements and take up a lot of space on the screen. You can double-click again to expand the element. In addition, you can use the menu commands Elements !WebObjects !Expand All or Elements !WebObjects !Collapse All to expand or collapse all the dynamic elements in the window.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements13.md)

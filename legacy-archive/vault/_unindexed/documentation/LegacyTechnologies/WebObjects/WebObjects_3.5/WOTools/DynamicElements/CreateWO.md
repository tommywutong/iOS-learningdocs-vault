---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/CreateWO.htm
archived_at: '2026-07-15T07:56:23.092431Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](Inspctrs.md)

# Creating Other WebObjects

!
You use this toolbar to create all dynamic elements other than form-based elements. This section provides some general information about using these elements. Each element is described in more detail in its own section.
To create a dynamic element, you click its toolbar icon. One thing to be aware of is what happens when there are already elements selected when you create the element:

- Some dynamic elements (WOHyperlink, WOConditional, WORepetition, custom WebObjects and generic WebObjects) can contain other elements. In this case, the selected elements appear with the new element "wrapped" around it.
- Other dynamic elements (WOString, WOImage, WOActiveImage, and WOApplet) can't contain other elements. When you create one, it replaces whatever was selected.

The first six dynamic element types (all those except for WOImage, WOActiveImage, and WOApplet) display with a pair of icons surrounding the element (and possibly other icons in between). For example, when you create a repetition, it appears like this in the component window:!
To bind a dynamic element, you drag from an item in the object browser to one of the outer icons. The Inspector appears, allowing you to complete the binding. See ["Binding Elements"](Binding.md#apple-gy2tioi) for more information.

You can double-click one of the icons to collapse the element into a single icon:
!
Collapsing can be desirable when you have dynamic elements that contain other elements and take up a lot of space on the screen. You can double-click again to expand the element. In addition, you can use the menu commands Elements !WebObjects !Expand All or Elements !WebObjects !Collapse All to expand or collapse all the dynamic elements in the window.

[!Table of Contents](DynElTOC.md) [!Next Section](DynString.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

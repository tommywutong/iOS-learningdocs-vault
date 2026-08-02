---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/CustomWO.htm
archived_at: '2026-07-15T07:56:25.060799Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](Cndnls.md)[Previous
Section](Cndnls.md) 

## Custom WebObjects

You use custom WebObjects for two main purposes:

- To implement WebObjects element classes not directly supported by WebObjects
  Builder. 
- To implement reusable components (see ["Reusable
  Components"](ReuseCmp.md#apple-gezdambq) for more details).

To create a custom WebObject:

1. Click ! in the toolbar. 

A template for a custom WebObject appears at the insertion point.

2. In the Custom WebObject Inspector, specify the element class. 
!

The WebObject Class combo box allows you to type the class name or select
it from the components listed in the pop-up menu. This menu lists all components
that are in the current project and frameworks. For example, the components
listed in the menu above (WOSimpleArrayDisplay, WOSortOrder, and so forth)
are defined in the WOExtensions framework, which is included in your project
by default.

If WebObjects Builder recognizes the element class, it automatically
displays its attributes. Otherwise, you can add them by clicking Add Attribute.

The WOExtensions palette (see ["Palettes"](../Editing/Pallette.md#apple-geytcnjv))
contains several pre-defined custom WebObjects elements you can use in
a component.

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](GenWO.md)[Next
Section](GenWO.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements17.html
archived_at: '2026-07-18T01:25:44.804515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements16.md)

## Custom WebObjects

You use custom WebObjects for two main purposes:

- To implement WebObjects element classes not directly supported by WebObjects Builder.
- To implement reusable components (see ["Reusable Components"](Reusable%20Components.md#apple-gezdambq) for more details).

To create a custom WebObject:

- Click ! in the toolbar.

A template for a custom WebObject appears at the insertion point.

- In the Custom WebObject Inspector, specify the element class.

!

The WebObject Class combo box allows you to type the class name or select it from the components listed in the pop-up menu. This menu lists all components that are in the current project and frameworks. For example, the components listed in the menu above (WOSimpleArrayDisplay, WOSortOrder, and so forth) are defined in the WOExtensions framework, which is included in your project by default.

If WebObjects Builder recognizes the element class, it automatically displays its attributes. Otherwise, you can add them by clicking Add Attribute.

The WOExtensions palette (see ["Palettes"](Palettes.md#apple-geytcnjv)) contains several pre-defined custom WebObjects elements you can use in a component.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements18.md)

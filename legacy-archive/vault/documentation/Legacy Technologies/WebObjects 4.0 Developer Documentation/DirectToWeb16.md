---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb16.html
archived_at: '2026-07-18T01:24:34.614922Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb15.md)

## Setting Which Properties are Displayed

The Customize Properties display of the WebAssistant enables you to specify which properties of an entity appear in a page (or component) and the order in which these properties appear. Most of the user-interface elements for accomplishing these things are in the left half of the display; note the Hide and Show columns along with their associated buttons in the following example:

!

All the entity's properties (attributes and relationships) are listed in the Show column, in the order in which they are displayed in the page. Properties in the Hide column are not displayed in the page. For each property, you can:

- Move it to the Hide column it by double-clicking it or by selecting it and clicking the left arrow. Likewise, if a property is hidden, you can show it by double-clicking it or by selecting it and clicking the right arrow.
- Move it up or down in the list by clicking the up and down arrows. This changes the order of appearance of the properties in the page (left to right or top to bottom, depending on the component).

By default, the WebAssistant shows only class properties. If you want to show a custom method or a keypath, click the Add button. A dialog box is displayed in which you can entery your custom key or key path (for example, "studio.budget").
You can also change the title for a property by editing the string in the Display Name field. This change only affects the way the entity is labeled in the page, and has no effect on the actual entity name.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb17.md)

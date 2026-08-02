---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb17.html
archived_at: '2026-07-18T01:24:36.752352Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb16.md)

## Changing How Properties Are Displayed

You can use the Customize Properties display of the WebAssistant to specify various display characteristics of properties, such as formatting, color, alignment, and the representation of to-many relationships. The fields and controls for setting these characteristics are on the right half of the display. Here is an example:

!

Let's go over the various elements of this part of the user interface:

- At the top is the name of the selected property and under this, in parentheses, is its data type. The data type determines the set of display components available for use. You cannot edit this information directly (however, you can edit where it is specified in the model file by using EOModler).
- Under the property name and data type is the Display field, which holds the title of the property for the current page and entity. As discussed in ["Setting Which Properties are Displayed")](DirectToWeb16.md#apple-geydqmrz), you can edit this string.
- The icon to the right of the Display field shows whether the selected property is an attribute ! or a relationship !. The list of available display components differs depending on whether the property is an attribute or a relationship.
- The WOComponent group (or "box") contains a pop-up menu showing the name of the component that is used to display the selected property in the current page. From this menu you can choose a different component to display the property. When you choose a display component, the set of controls and fields in the WOComponent group can change.

The items in the WOComponent pop-up menu identify reusable components in the Direct to Web framework which are used to generate the pages you see in your application. Each property in a page of any type is initially shown in a default way for that type and is based on a certain component.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb18.md)

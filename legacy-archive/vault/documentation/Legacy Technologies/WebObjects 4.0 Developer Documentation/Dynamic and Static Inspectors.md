---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements11.html
archived_at: '2026-07-18T01:25:33.249675Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Creating%20Form-Based%20Dynamic%20Elements.md)

# Dynamic and Static Inspectors

Most dynamic elements have static HTML counterparts (with the exception of abstract dynamic elements, such as: WOString, WORepetition, WOConditional, and WOCustom.) The Inspector for these elements has two states:

- The Dynamic Inspector, which you use to set the bindings for the element (see ["Binding Elements"](Binding%20Elements-2.md#apple-gy2tioi)).
- The Static Inspector, which you use to set the HTML attributes for the element's static counterpart.
!

This example shows the Inspector for a dynamic text area element. It displays the bindable attributes for this element. If you select Static Inspector from the pop-up list, the Text Area Inspector appears. This is the same Inspector you would see for a static text area element (<TEXTAREA>) and allows you to set its HTML attributes (such as COLS or ROWS).
__Note:__  You can also set the HTML attributes using the Dynamic Inspector. The Static Inspector is provided for convenience only.!
To switch back to the WOText Inspector, select Dynamic Inspector from the pop-up list.
In addition, you can convert any dynamic element into its static counterpart, or vice versa:

- When inspecting a dynamic element, if you click Make Static, the element becomes its static counterpart (if it has one), and the Static Inspector appears.
- When inspecting a static element, if you click Make Dynamic, the element becomes its dynamic counterpart. Both the Static and Dynamic Inspectors are now available.

The following table shows the dynamic counterpart for each static element.

|  __Static Element__ |  Dynamic Counterpart |
|  Image |  WOImage, WOActiveImage |
|  Form |  WOForm |
|  Textfield |  WOTextField |
|  Text Area |  WOText |
|  Button |  WOSubmitButton, WOResetButton, WOImageButton |
|  Checkbox |  WOCheckBox |
|  Radio Button |  WORadioButton |
|  Select |  WOBrowser, WOPopupButton |
|  Hyperlink |  WOHyperlink |
|  Applet |  WOApplet |
|  Other |  Generic WebObject |

```
```


If you convert a static element to its dynamic counterpart by clicking Make Dynamic, and there is no direct counterpart, the element becomes a generic WebObject whose element name is the HTML tag for the static element (see ["Generic WebObjects"](DynamicElements18.md#apple-gy2tsoi)). In this figure, a list element (<UL>) has been converted to a generic WebObject element.

!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Creating%20Other%20WebObjects.md)

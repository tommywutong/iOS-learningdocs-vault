---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/Inspctrs.htm
archived_at: '2026-07-15T07:56:34.107004Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](FormBase.md)

# Dynamic and Static Inspectors

Most dynamic elements have static HTML counterparts. (The exceptions are the abstract dynamic elements: WOString, WORepetition, WOConditional, and WOCustom.) The Inspector for these elements has two states:

- The Dynamic Inspector, which you use to set the bindings for the element (see ["Binding Elements"](Binding.md#apple-gy2tioi)).
- The Static Inspector, which you use to set the HTML attributes for the element's static counterpart.
!

This example shows the Inspector for a dynamic text area element. It displays the bindable attributes for this element. If you select Static Inspector from the pop-up list, the Text Area Inspector appears. This is the same Inspector you would see for a static text area element (<TEXTAREA>) and allows you to set its HTML attributes (such as COLS or ROWS).!
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


If you convert a static element to its dynamic counterpart by clicking Make Dynamic, and there is no direct counterpart, the element becomes a generic WebObject whose element name is the HTML tag for the static element (see ["Generic WebObjects"](GenWO.md#apple-gy2tsoi)). In this figure, a list element (<UL>) has been converted to a generic WebObject element.

!

[!Table of Contents](DynElTOC.md) [!Next Section](CreateWO.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.4d.html
archived_at: '2026-07-15T08:10:48.634025Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Dynamic%20and%20Static%20Inspectors.md) [!](Dynamic%20Strings.md)

---

#   Creating Other WebObjects

!

You use this toolbar to create all dynamic elements other than form-based elements. This section provides some general information about using these elements. Each element is described in more detail in its own section.

To create a dynamic element, you click its toolbar icon. One thing to be aware of is what happens when there are already elements selected when you create the element:

- 

  Some dynamic elements (WOHyperlink, WOConditional, WORepetition, custom WebObjects and generic WebObjects) can contain other elements. In this case, the selected elements appear with the new element "wrapped" around it.
- 

  Other dynamic elements (WOString, WOImage, WOActiveImage, and WOApplet) can't contain other elements. When you create one, it replaces whatever was selected.

The dynamic element types in the toolbar except for WOImage, WOActiveImage, and WOApplet display with a pair of icons surrounding the element (and possibly other icons in between). For example, when you create a repetition, it appears like this in the component window:

!

To bind a dynamic element, you drag from an item in the object browser to one of the outer icons. The attribute menu appears, allowing you to complete the binding. See [Binding Elements](Binding%20Elements-2.md#apple-gmztcmzq)
for more information.

#### [Dynamic Strings](Dynamic%20Strings.md#apple-obtwmslehu3dgnru)

#### [Dynamic Hyperlinks](Dynamic%20Hyperlinks.md#apple-obtwmslehu3dinbr)

#### [Repetitions](Repetitions.md#apple-obtwmslehuytanjvga)

#### [Conditionals](Conditionals.md#apple-obtwmslehu4tanbt)

#### [Dynamic Images](Dynamic%20Images.md#apple-obtwmslehu3tgnbx)

#### [Generic WebObjects](Generic%20WebObjects.md#apple-obtwmslehuytimjugy)

#### [WOComponentContent](WOComponentContent.md#apple-obtwmslehuytimrwha)

#### [WOApplets](WOApplets.md#apple-obtwmslehuytimruha)

#### [Custom WebObjects](Custom%20WebObjects.md#apple-obtwmslehuytimjqg4)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Dynamic%20and%20Static%20Inspectors.md) [!](Dynamic%20Strings.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

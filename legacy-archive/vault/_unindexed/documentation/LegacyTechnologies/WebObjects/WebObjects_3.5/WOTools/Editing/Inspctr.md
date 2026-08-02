---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/Inspctr.htm
archived_at: '2026-07-15T07:57:11.665138Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/SelElemhtm)[Previous
Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Editing/SelElemhtm) 

# The Inspector

You use the Inspector to set HTML attributes of the
elements in your component.

To open the Inspector, click !.
The Inspector's title and contents reflect the element you've selected
in the component window. Each element has its own Inspector that allows
you to set properties appropriate for the element. For example, the Heading
Inspector shown here allows you to set the level of a heading element.
Other elements have different properties that you can set.

!

The top of the window shows the _element path_ to
the selected element. Any element can be contained in a hierarchy of several
levels of elements and can in turn contain other elements. Here, the element
path shows that the heading element is contained in the page element, which
is the top level of the hierarchy. When you click an icon in the element
path, the appropriate Inspector for that element appears. In this case,
if you click the page icon, the Page Attributes Inspector appears. (__Note:__
If no element is selected, the Inspector shows Page Attributes by default.)

The Make Dynamic button in the Inspector allows you
to convert an HTML element into a dynamic WebObjects element. Dynamic elements
have a Make Static button, which allows them to be converted to their static
counterparts. This feature is discussed in more detail in ["Dynamic
and Static Inspectors"](../DynamicElements/Inspctrs.md#apple-he4tooa).

[!](EditTOC.md)[Table
of Contents](EditTOC.md) [!](StrucEle.md)[Next
Section](StrucEle.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

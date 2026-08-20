---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing9.html
archived_at: '2026-07-18T01:27:31.068417Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Editing8.md)

# The Inspector

You use the Inspector to set HTML attributes of the elements in your component.
To open the Inspector, click !. The Inspector's title and contents reflect the element you've selected in the component window. Each element has its own Inspector that allows you to set properties appropriate for the element. For example, the Heading Inspector shown here allows you to set the level of a heading element. Other elements have different properties that you can set.

!

The top of the window shows the _element path_to the selected element. Any element can be contained in a hierarchy of several levels of elements and can in turn contain other elements. Here, the element path shows that the heading element is contained in the page element, which is the top level of the hierarchy. When you click an icon in the element path, the appropriate Inspector for that element appears. In this case, if you click the page icon, the Page Attributes Inspector appears. (__Note:__ If no element is selected, the Inspector shows Page Attributes by default.)
The Make Dynamic button in the Inspector allows you to convert an HTML element into a dynamic WebObjects element. Dynamic elements have a Make Static button, which allows them to be converted to their static counterparts. This feature is discussed in more detail in ["Dynamic and Static Inspectors"](Dynamic%20and%20Static%20Inspectors.md#apple-he4tooa).

__Important:__ When you type a value (such as number of pixels) in one of the Inspector's fields, you must press Enter for the change to take effect. In other words, if you simply type the value and move to another field, the change does not take place.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Structure%20Elements.md)

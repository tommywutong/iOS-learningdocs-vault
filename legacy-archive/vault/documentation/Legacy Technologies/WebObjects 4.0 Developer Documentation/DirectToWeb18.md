---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb18.html
archived_at: '2026-07-18T01:24:39.037602Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb17.md)

### Textual Attributes and Formatting

The display components available for the currently selected property offer characteristics suitable to the data type and function of the attribute. A few examples might help to clarify this statement:

- If the data type of the attribute is an NSString (or String in Java) but it is a URL, then the DisplayHyperlink or DisplayMailTo components could be what you want.
- If the attribute is a date (NSCalendarDate), then you might choose the DisplayString component and provide format specifiers to have the date formatted in a certain way.
- Similarly, if the attribute is a currency value (NSNumber), you might want to use the DisplayNumber component and format the display of the attribute with two decimal positions and a leading dollar sign.
- If you want to highlight a certain column of values in a table by giving them a different color, then you could choose the DisplayStyledString component which lets you apply a color to a property.

You can click the Info button in the WebAssistant to get a short description of the currently selected display component.
The three most common display characteristics for properties are alignment, formatting, and color. Each of these has their own controls or fields in the WOComponent group:

- __Alignment__. Choose Right, Center, or Left from the pop-up menu to specify the alignment of text within a cell of a table.
- __Formatter__. You can have your application display some types of data, such as dates and numbers, as formatted strings. For example, the date "Sat 4 Jul 98" can be also represented as "July 4, 1998." The number one thousand can be represented either as "1,000" or "1.000", depending on the locale. There are different format specifiers for dates and numbers; check the reference documentation for the NSDateFormatter and NSNumberFormatter classes for details.
- __Color__. To change the color of text, either move the sliders to the right of the sample color or enter hexadecimal numbers in the field above the sliders. The color specification is RGB-based (that is, a specific mixture of red, green, and blue). The top slider manipulates red saturation, the middle slider is for green, and the bottom slider is for blue. The three pairs of hexadecimal digits after the number sign in the field represent (left to right) saturation levels of red, green, and blue.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb19.md)

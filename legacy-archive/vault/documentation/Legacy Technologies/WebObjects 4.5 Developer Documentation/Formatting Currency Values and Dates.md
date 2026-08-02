---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.1f.html
archived_at: '2026-07-15T08:09:00.186584Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Creating%20the%20User%20Interface.md) [!](Creating%20the%20User%20Interface.md) [!](Adding%20Action%20Methods.md)

---

#  Formatting Currency Values and Dates

When an attribute is defined in your model as having the internal type Number, a currency formatter is automatically added to any control with which the attribute is associated. Likewise, when an attribute has an NSGregorianDate type, date formatters are added to controls associated with it.

Not all adaptors map, say, the __budget__ attribute to the Number data type. In that case, you won't automatically get currency formatting in the column. You can fix this problem either by setting __budget__'s internal type to be Number in the model, or you can add a currency formatter to the column (as described in [Writing Derived Methods](Writing%20Derived%20Methods.md#apple-ge4dgmzq)
).

Once a control has a formatter, you can use the Inspector to change it.

1. 

   Set field formatting.

   Select the __Budget__
   column head in the table view, and display the Formatter view of the NSTableColumn Inspector.

   Change the format to a standard currency format.

   !

   Do not set the format to show negative values in red. The JFC currently does not implement colored text.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Creating%20the%20User%20Interface.md) [!](Creating%20the%20User%20Interface.md) [!](Adding%20Action%20Methods.md)

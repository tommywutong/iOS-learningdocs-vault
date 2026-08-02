---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.3c.html
archived_at: '2026-07-15T08:07:53.965048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Refining%20Main.wo.md) [!](Specifying%20Default%20Values%20for%20New%20Enterprise%20Objects.md) [!](Setting%20a%20Number%20Format.md)

---

#  Setting a Date Format

To change the way that dates are displayed, you assign a date format to the element that displays the dates.

1. 

   Using WebObjects Builder, inspect the __dateReleased__ text field, which is near the bottom of the Main component window.

   Notice that the text field has a __dateformat__ attribute that is bound to the string "%m/%d/%y". This binding tells the text field that it's displaying dates and describes how to format them. The %m conversion specifier stands for month as a decimal number, %d stands for day of the month, and %y stands for year without century.
2. 

   Click the combo box on the right side of the binding column. Choose "%d %B %Y".

   This date format displays dates as 14 Jan 2005. The %b conversion specifier stands for abbreviated month name, and %Y stands for year with century. You can create your own date formats with any of the conversion specifiers defined for dates. For more information, see the NSGregorianDate class specification in the _Foundation Framework Reference_.

   !

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Refining%20Main.wo.md) [!](Specifying%20Default%20Values%20for%20New%20Enterprise%20Objects.md) [!](Setting%20a%20Number%20Format.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

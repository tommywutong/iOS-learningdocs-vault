---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies22.html
archived_at: '2026-07-15T07:54:23.267175Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies21.md)

## Setting a Date Format

To change the way that dates are displayed, you assign a date format to the element that displays the dates.

- Inspect the __dateReleased__ text field, which is near the bottom of the Main component window.

Notice that the text field has a __dateformat__ attribute that is bound to the string "%m/%d/%y". This binding tells the text field that it's displaying dates and describes how to format them. The %m conversion specifier stands for month as a decimal number, %d stands for day of the month, and %y stands for year without century.

- Change the __dateformat__ value to the string (including the quotes) "%d %b %Y".

This date format displays dates such as 3 Sep 1997. The %b conversion specifier stands for abbreviated month name, and %Y stands for year with century. You can create your own date formats with any of the conversion specifiers defined for dates. For more information, see the CalendarDate class specification in the _Foundation Framework Reference_.

!

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies23.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

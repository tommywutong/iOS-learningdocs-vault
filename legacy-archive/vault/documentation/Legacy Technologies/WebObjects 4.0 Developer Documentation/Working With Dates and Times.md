---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Foundation7.html
archived_at: '2026-07-18T01:20:13.009211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Previous Section](Commonly%20Used%20Dictionary%20Methods.md)

# Working With Dates and Times

NSCalendarDate objects represent dates and times. These objects are especially suited for representing and manipulating dates according to Western calendrical systems, primarily the Gregorian.
The methods provided by NSCalendarDate are described in more detail in ["Commonly Used Date Methods"](Commonly%20Used%20Date%20Methods.md#apple-gezdoma).

## The Calendar Format

Each NSCalendarDate object has a calendar format associated with it. This format is a string that contains date-conversion specifiers very similar to those used in the standard C library function __strftime()__. NSCalendarDate interprets dates that are represented as strings conforming to this format. You can set the default format for an NSCalendarDate object either at initialization time or by using the __setCalendarFormat:__ method. Several methods allow you to specify formats other than the one bound to the object.

## Date Conversion Specifiers

The date conversion specifiers cover a range of date conventions:

|  __Conversion Specifier__ |  Argument Type |
|  %% |  a '%' character |
|  %A, %a |  full and abbreviated weekday name, respectively |
|  %B, %b |  full and abbreviated month name, respectively |
|  %c |  date and time designation for the locale |
|  %d |  day of the month as a decimal number (01-31) |
|  %F |  milliseconds as a decimal number (000-999) |
|  %H, %I |  hour based on a 24-hour or 12-hour clock as a decimal number, respectively. (00-23 or 01-12) |
|  %j |  day of the year as a decimal number (001-366) |
|  %M |  minute as a decimal number (00-59) |
|  %m |  month as a decimal number (01-12) |
|  %p |  AM/PM designation for the locale |
|  %S |  second as a decimal number (00-59) |
|  %w |  weekday as a decimal number (0-6), where Sunday is 0 |
|  %x |  date using date representation for the locale |
|  %X |  time using time representation for the locale |
|  %Y, %y |  year with century (such as 1990) and year without century (00-99), respectively |
|  %Z, %z |  time zone abbreviation (such as PDT) and time zone offset in hours and minutes from GMT (HHMM), respectively |

```
```

[!Table of Contents](WebScript%20Programmer%27s%20Quick%20Reference%20to%20Foundation%20Classes.md) [!Next Section](Commonly%20Used%20Date%20Methods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

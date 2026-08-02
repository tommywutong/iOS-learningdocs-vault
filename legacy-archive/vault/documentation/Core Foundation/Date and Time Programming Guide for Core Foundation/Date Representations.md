---
title: Date and Time Programming Guide for Core Foundation
apple_id: 10000125i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/Concepts/DataReps.html
archived_at: '2026-07-15T07:22:17.651402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Date and Time Programming Guide for Core Foundation](Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Time%20Zones.md)[Previous](Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md)

# Date Representations

Core Foundation allows you to work with
five different representations of time:

- CFAbsoluteTime, a specific point in time relative
  to 1 January 2001 00:00:00 GMT
- CFTimeInterval, an interval of time in seconds
- CFGregorianDate, a specific point in time represented using
  the Gregorian calender
- CFGregorianUnits, an interval of time in one or more of the
  units used in the Gregorian calendar
- CFDate, an absolute time in the format of a Core Foundation
  opaque type

CFAbsoluteTime is useful when you need to refer to a specific
point in time. A CFAbsoluteTime value represents time as a number
of seconds relative to the reference date of 1 January, 2001 00:00:00
GMT. A positive value represents a date after the reference date,
a negative value represents a date before it.

Absolute time can be confusing at first because an absolute
time value is literally a time interval (the number of seconds since
the reference date), but it is interpreted as a specific instant
in time. For example, the absolute time -32940326 indicates both
a date and time—December 16th, 1999 at 17:54:34. An absolute time
value cannot be used to refer to a date or a clock time independently,
it always includes both.

CFAbsoluteTime is implemented as a `double` and
can be compared with another absolute time using the standard C
comparison operators.

CFTimeInterval is appropriate when you need to measure duration.
A CFTimeInterval represents elapsed time in seconds. As with CFAbsoluteTime,
a CFTimeInterval is implemented using the C type `double` and
so you can compare two CFTimeInterval values using the standard
C comparison operators.

CFGregorianDate represents time using the Gregorian calendar
that has been in general use in Europe and the Western Hemisphere
since 1582. A CFGregorianDate is implemented as a C structure with
separate fields for years, months, days, hours, minutes, and seconds.
You can check any or all of the fields of a CFGregorianDate for
validity. A Gregorian date can also be converted to and from an
absolute time.

CFGregorianUnits is analogous to a CFTimeInterval in that
it represents a duration rather than a specific point in time. Like
CFGregorianDate, CFGregorianUnits is implemented as a C structure,
but the data types of the fields are different to allow for larger
values. For example, a CFGregorianDate will never have more than
52 weeks, or 24 hours, so the fields of the CFGregorianDate structure
are implemented using the smallest data type appropriate for its
maximum value. Because CFGregorianUnits is intended to represent arbitrary
time intervals, it is implemented with 32 bit integers (except for
seconds, which is of type `double` to
allow for fractional values).

If you need to place a date in a Core Foundation property
list, it must be of type CFDate. A CFDate object is simply an absolute
time “wrapped” as a Core Foundation opaque type. A Gregorian
date must first be converted to an absolute time, and then it can
become a CFDate object. A CFDate object can be compared with another
CFDate using a standard Core Foundation comparison function. Note
that a CFDate can only be created with an absolute time, CFTimeInterval
values are not supported. Use a CFNumber to wrap ordinary floating
point values like a CFTimeInterval. CFDate objects are immutable.

[Next](Time%20Zones.md)[Previous](Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md)


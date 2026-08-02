---
title: Date and Time Programming Guide for Core Foundation
apple_id: 10000125i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/Tasks/UsingDates.html
archived_at: '2026-07-15T07:22:19.160208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Date and Time Programming Guide for Core Foundation](Introduction%20to%20Dates%20and%20Times%20Programming%20Guide%20for%20Core%20Foundation.md)


[Next](Document%20Revision%20History.md)[Previous](Time%20Zones.md)

# Using Dates

This task contains examples on creating, comparing, and converting
dates. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dcljrgaydsnrzfvbeeq2fivduqsq) shows you how to get the current absolute time and
convert it into a CFDate object.

__Listing 1__  Creating
a CFDate object

```
CFAbsoluteTime      absTime;
CFDateRef           aCFDate;

absTime = CFAbsoluteTimeGetCurrent();
aCFDate = CFDateCreate(kCFAllocatorDefault, absTime);
```

To compare two dates, use the compare function `CFDateCompare` as
shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dcljrgaytamrqfvbuuqsdjjdesqy).

__Listing 2__  Comparing
two CFDate objects

```
// Standard Core Foundation comparison result.
CFComparisonResult result;

// Create two CFDates from absolute time.
date1 = CFDateCreate(kCFAllocatorDefault, CFAbsoluteTimeGetCurrent());
date2 = CFDateCreate(kCFAllocatorDefault, CFAbsoluteTimeGetCurrent());

// Pass NULL for the context param.
result = CFDateCompare(date1, date2, NULL);

switch (result) {
    case kCFCompareLessThan:
        printf("date1 is before date2!\n");
        break;
    case kCFCompareEqualTo:
        printf("date1 is the same as date2!\n");
        break;
    case kCFCompareGreaterThan:
        printf("date1 is after date2!\n");
        break;
    }
```

The `CFDateCompare` function
performs exact comparisons, which means it detects sub-second differences
between dates. You might want to compare dates with a less fine granularity.
For example, you might want to consider two dates equal if they
are within one minute of each other. This can be accomplished by
simply converting the CFDates to absolute time and comparing the
two floating-point values using your fuzziness factor. To compare
Gregorian units like month or week, you can convert both CFDates
to CFGregorianDate and compare the appropriate fields. Converting
absolute time to and from Gregorian dates is quite simple. [Listing 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dcljrgaytcnjwfvbeeq2kifeumrq) demonstrates
how to do this.

__Listing 3__  Working
with Gregorian dates

```
Boolean             status;
CFGregorianDate     gregDate;
CFAbsoluteTime      absTime;

// Construct a Gregorian date.
gregDate.year = 1999;
gregDate.month = 11;
gregDate.day = 23;
gregDate.hour = 17;
gregDate.minute = 33;
gregDate.second = 22.7;

// Check the validity of the date.
status = CFGregorianDateIsValid(gregDate, kCFGregorianAllUnits);
printf("Is my Gregorian date valid? %d\n", status);

// Convert the Gregorian date to absolute time.
absTime = CFGregorianDateGetAbsoluteTime(gregDate, NULL);
printf("The Absolute Time from a Gregorian date is: %d\n", absTime);
```

[Next](Document%20Revision%20History.md)[Previous](Time%20Zones.md)


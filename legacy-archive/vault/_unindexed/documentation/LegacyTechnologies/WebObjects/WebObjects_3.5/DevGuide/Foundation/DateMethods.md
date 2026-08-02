---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Foundation/DateMethods.html
archived_at: '2026-07-15T07:51:38.216847Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](FoundationTOC.md) [!Previous Section](DateIntro.md)

# Commonly Used Date Methods

The following sections list some of the most commonly used methods of NSCalendarDate, grouped according to function.

## Creating Dates

The methods in this section are class methods, denoted by the plus sign (+). You use class methods to send messages to a class-in this case, NSCalendarDate. For more information on class methods, see ["Sending a Message to a Class"](../WebScript/MessageToClass.md#apple-gi2ts).

**__+ calendarDate__**
: Returns an NSCalendarDate initialized to the current date and time.

**__+ dateWithString:calendarFormat:__**
: Returns an NSCalendarDate initialized to the date in a provided string, and sets the new NSCalendarDate's calendar format to the specified format. The date string must match the provided format exactly. See ["Date Conversion Specifiers"](DateIntro.md#apple-guytemy) for more detailed information on formats used by NSCalendarDate.

## Adjusting a Date

**__- dateByAddingYears:months:days:hours:minutes:seconds:__**
: Returns an NSCalendarDate derived from the receiver by adding a specified number of years, months, days, hours, minutes, and seconds.

## Representing Dates as Strings

**__- description__**
: Returns a string representation of the NSCalendarDate formatted according to the NSCalendarDate's default calendar format.

**__- descriptionWithCalendarFormat:__**
: Returns a string representation of the receiver formatted according to the provided format string.

**__- calendarFormat__**
: Returns a string that indicates the receiver's default calendar format. See ["Date Conversion Specifiers"](DateIntro.md#apple-guytemy) for more detailed information on formats used by NSCalendarDate.

**__- setCalendarFormat:__**
: Set the receiver's default calendar format to the provided string.

## Retrieving Date Elements

**__- dayOfWeek__**
: Returns a number that indicates the NSCalendarDate's day of the week (0-6).

**__- dayOfMonth__**
: Returns the NSCalendarDate's day of the month (1-31).

**__- dayOfYear__**
: Returns a number that indicates the NSCalendarDate's day of the year (1-366).

**__- dayOfCommonEra__**
: Returns the NSCalendarDate's number of days since the beginning of the Common Era. The base year of the Common Era is 1 A.C.E. (which is the same as 1 A.D.).

**__- monthOfYear__**
: Returns a number that indicates the NSCalendarDate's month of the year (1-12).

**__- yearOfCommonEra__**
: Returns the NSCalendarDate's year value (including the century).

**__- hourOfDay__**
: Returns the NSCalendarDate's hour value (0-23).

**__- minuteOfHour__**
: Returns the NSCalendarDate's minutes value (0-59).

**__- secondOfMinute__**
: Returns the NSCalendarDate's seconds value (0-59).

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
title: NSDateComponents
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents.json'
content_hash: 'sha256:4cdaee31534910a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDateComponents

<sub>Class</sub>

An object that specifies a date or time in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDateComponents
```

## Overview

In Swift, this object bridges to [DateComponents](datecomponents.md); use [NSDateComponents](nsdatecomponents.md) when you need reference semantics or other Foundation-specific behavior.

[NSDateComponents](nsdatecomponents.md) encapsulates the components of a date in an extendable, object-oriented manner. It’s used to specify a date by providing the temporal components that make up a date and time: hour, minutes, seconds, day, month, year, and so on. You can also use it to specify a duration of time, for example, 5 hours and 16 minutes. An [NSDateComponents](nsdatecomponents.md) object is not required to define all the component fields. When a new instance of [NSDateComponents](nsdatecomponents.md) is created, the date components are set to [NSDateComponentUndefined](nsdatecomponentundefined.md).

> [!important] Important
> An [NSDateComponents](nsdatecomponents.md) object is meaningless in itself; you need to know what calendar it is interpreted against, and you need to know whether the values are absolute values of the units, or quantities of the units.

An instance of [NSDateComponents](nsdatecomponents.md) is not responsible for answering questions about a date beyond the information with which it was initialized. For example, if you initialize one with May 4, 2017, its weekday is [NSDateComponentUndefined](nsdatecomponentundefined.md), not Thursday. To get the correct day of the week, you must create a suitable instance of [NSCalendar](nscalendar.md), create an [NSDate](nsdate.md) object using [- dateFromComponents:](<nscalendar/date(from_).md>) and then use [- components:fromDate:](<nscalendar/components(__from_).md>) to retrieve the weekday—as illustrated in the following example.

**Swift**

```swift
let dateComponents = NSDateComponents()
dateComponents.day = 4
dateComponents.month = 5
dateComponents.year = 2017

if let gregorianCalendar = NSCalendar(calendarIdentifier: .gregorian),
    let date = gregorianCalendar.date(from: dateComponents as DateComponents) {
    let weekday = gregorianCalendar.component(.weekday, from: date)
    print(weekday) // 5, which corresponds to Thursday in the Gregorian Calendar
}

```

**Objective-C**

```objc
NSDateComponents *dateComponents = [[NSDateComponents alloc] init];
dateComponents.day = 4;
dateComponents.month = 5;
dateComponents.year = 2017;
 
NSCalendar *gregorianCalendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
NSDate *date = [gregorianCalendar dateFromComponents:dateComponents];
 
NSInteger weekday = [gregorianCalendar component:NSCalendarUnitWeekday fromDate:date];
NSLog(@"%d", weekday); // 5, which corresponds to Thursday in the Gregorian Calendar
```

For more details, see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

> [!important] Important
> The Swift overlay to the Foundation framework provides the [DateComponents](datecomponents.md) structure, which bridges to the [NSDateComponents](nsdatecomponents.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Setting a Calendar and Time Zone

- [calendar](nsdatecomponents/calendar.md) — The calendar used to interpret the date components.
- [timeZone](nsdatecomponents/timezone.md) — The time zone used to interpret the date components.

### Validating a Date

- [validDate](nsdatecomponents/isvaliddate.md) — A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [- isValidDateInCalendar:](<nsdatecomponents/isvaliddate(in_).md>) — Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [date](nsdatecomponents/date.md) — The date calculated from the current components using the stored calendar.
- [Undefined Components](1430344-undefined-components.md) — Constants that denote that the value of a date component is undefined.

### Accessing Years and Months

- [era](nsdatecomponents/era.md) — The number of eras.
- [year](nsdatecomponents/year.md) — The number of years.
- [yearForWeekOfYear](nsdatecomponents/yearforweekofyear.md) — The ISO 8601 week-numbering year.
- [quarter](nsdatecomponents/quarter.md) — The number of quarters.
- [month](nsdatecomponents/month.md) — The number of months.
- [leapMonth](nsdatecomponents/isleapmonth.md) — A Boolean value that indicates whether the month is a leap month.

### Accessing Weeks and Days

- [weekday](nsdatecomponents/weekday.md) — The number of the weekdays.
- [weekdayOrdinal](nsdatecomponents/weekdayordinal.md) — The ordinal number of weekdays.
- [weekOfMonth](nsdatecomponents/weekofmonth.md) — The week number of the months.
- [weekOfYear](nsdatecomponents/weekofyear.md) — The ISO 8601 week date of the year.
- [day](nsdatecomponents/day.md) — The number of days.
- [- week](<nsdatecomponents/week().md>) — Returns the number of weeks. _(deprecated)_
- [- setWeek:](<nsdatecomponents/setweek(__).md>) — Sets the number of weeks. _(deprecated)_

### Accessing Hours and Seconds

- [hour](nsdatecomponents/hour.md) — The number of hour units for the receiver.
- [minute](nsdatecomponents/minute.md) — The number of minute units for the receiver.
- [second](nsdatecomponents/second.md) — The number of second units for the receiver.
- [nanosecond](nsdatecomponents/nanosecond.md) — The number of nanosecond units for the receiver.

### Accessing Components as Calendrical Units

- [- valueForComponent:](<nsdatecomponents/value(forcomponent_).md>) — Returns the value for a given calendar unit.
- [- setValue:forComponent:](<nsdatecomponents/setvalue(__forcomponent_).md>) — Sets a value for a given calendar unit.
- [Unit](nscalendar/unit.md) — Calendrical units such as year, month, day and hour.

### Initializers

- [init(coder:)](<nsdatecomponents/init(coder_).md>)

### Instance Properties

- [dayOfYear](nsdatecomponents/dayofyear.md) — The day of the year value of the date components.
- [repeatedDay](nsdatecomponents/isrepeatedday.md)

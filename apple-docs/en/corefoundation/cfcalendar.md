---
title: CFCalendar
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcalendar
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcalendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcalendar.json'
content_hash: 'sha256:09f5e0281167c28a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCalendar

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFCalendar
```

## Overview

The CFCalendar opaque type represents a calendar system. The associated API provides information about a calendar and supports calendrical computations such as determining the range of a given calendrical unit and adding units to a given absolute time.

CFAbsoluteTime is the operational lingua franca of CFCalendar—to do calendar arithmetic, you start and end with an absolute time; to convert between a decomposed date in one calendar and another calendar, you first convert to an absolute time. CFAbsoluteTime provides the absolute scale and epoch for dates and times, which can then be rendered into a particular calendar, for calendrical computations or user display.

In a calendar, day, week, weekday, month, and year numbers are generally 1-based, but there may be calendar-specific exceptions. Ordinal numbers, where they occur, are 1-based. Some calendars represented by this API may have to map their basic unit concepts into year/month/week/day/… nomenclature. For example, a calendar composed of 4 quarters in a year instead of 12 months uses the “month” unit to represent quarters. The particular values of the unit are defined by each calendar, and are not necessarily “consistent with” or have a “correspondence with,” values for that unit in another calendar. Several CFCalendar functions ([CFCalendarComposeAbsoluteTime](cfcalendarcomposeabsolutetime.md), [CFCalendarDecomposeAbsoluteTime](cfcalendardecomposeabsolutetime.md), [CFCalendarAddComponents](cfcalendaraddcomponents.md), and [CFCalendarGetComponentDifference](cfcalendargetcomponentdifference.md)) take a description string that describes the calendrical components provided in a varargs parameter area. You can provide as many components as you need (or choose to), in whatever order you choose. When there is incomplete information to compute an absolute time, default values similar to 0 and 1 are usually chosen by a calendar, but this is a calendar-specific choice. If you provide inconsistent information, calendar-specific disambiguation is performed (which may involve ignoring one or more of the parameters). The characters of the description string specify the units and order of the parameters which follow. The characters are adopted from the corresponding format characters used by CFDateFormatter when possible, as shown in below.

| Symbol | Meaning | Value Type |
|---|---|---|
| y | year | int |
| M | month | int |
| d | day | int |
| H | hour | int |
| m | minute | int |
| s | second | int |

Information related to formatting dates and times and name-related calendar information is managed by CFDateFormatter.

CFCalendar is subject to some limitations. There is no leap second handling—the existence of leap seconds is ignored as in the other CoreFoundation API. In general, historical accuracy of calendars is not guaranteed. There is currently no API for defining your own calendars.

CFCalendar is “toll-free bridged” with its Cocoa Foundation counterpart, NSCalendar. This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSCalendar *` parameter, you can pass in a `CFCalendarRef`, and in a function where you see a `CFCalendarRef` parameter, you can pass in an NSCalendar instance. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Calendar

- [CFCalendarCopyCurrent](<cfcalendarcopycurrent().md>) — Returns a copy of the logical calendar for the current user.
- [CFCalendarCreateWithIdentifier](<cfcalendarcreatewithidentifier(____).md>) — Returns a calendar object for the calendar identified by a calendar identifier.

### Getting Ranges of Units

- [CFCalendarGetRangeOfUnit](<cfcalendargetrangeofunit(________).md>) — Returns the range of values that one unit can take on within a larger unit during which a specific absolute time occurs.
- [CFCalendarGetOrdinalityOfUnit](<cfcalendargetordinalityofunit(________).md>) — Returns the ordinal number of a calendrical unit within a larger unit at a specified absolute time.
- [CFCalendarGetTimeRangeOfUnit](<cfcalendargettimerangeofunit(__________).md>) — Returns by reference the start time and duration of a given calendar unit that contains a given absolute time.
- [CFCalendarGetMaximumRangeOfUnit](<cfcalendargetmaximumrangeofunit(____).md>) — Returns the maximum range limits of the values that a specified unit can take on in a given calendar.
- [CFCalendarGetMinimumRangeOfUnit](<cfcalendargetminimumrangeofunit(____).md>) — Returns the minimum range limits of the values that a specified unit can take on in a given calendar.

### Getting and Setting the Time Zone

- [CFCalendarCopyTimeZone](<cfcalendarcopytimezone(__).md>) — Returns a time zone object for a specified calendar.
- [CFCalendarSetTimeZone](<cfcalendarsettimezone(____).md>) — Sets the time zone for a calendar.

### Getting the Identifier

- [CFCalendarGetIdentifier](<cfcalendargetidentifier(__).md>) — Returns the given calendar’s identifier.

### Getting and Setting the Locale

- [CFCalendarCopyLocale](<cfcalendarcopylocale(__).md>) — Returns a locale object for a specified calendar.
- [CFCalendarSetLocale](<cfcalendarsetlocale(____).md>) — Sets the locale for a calendar.

### Getting and Setting Day Information

- [CFCalendarGetFirstWeekday](<cfcalendargetfirstweekday(__).md>) — Returns the index of first weekday for a specified calendar.
- [CFCalendarSetFirstWeekday](<cfcalendarsetfirstweekday(____).md>) — Sets the first weekday for a calendar.
- [CFCalendarGetMinimumDaysInFirstWeek](<cfcalendargetminimumdaysinfirstweek(__).md>) — Returns the minimum number of days in the first week of a specified calendar.
- [CFCalendarSetMinimumDaysInFirstWeek](<cfcalendarsetminimumdaysinfirstweek(____).md>) — Sets the minimum number of days in the first week of a specified calendar.

### Getting the Type ID

- [CFCalendarGetTypeID](<cfcalendargettypeid().md>) — Returns the type identifier for the CFCalendar opaque type.

### Constants

- [CFCalendarUnit](cfcalendarunit.md) — CFCalendarUnit constants are used to specify calendrical units, such as day or month, in various calendar calculations.
- [Component Wrapping Options](1533520-component-wrapping-options.md) — The wrapping option specifies overflow behavior for calendar components in calendrical calculations

## See Also

### Related Documentation

- [Date and Time Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)
- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

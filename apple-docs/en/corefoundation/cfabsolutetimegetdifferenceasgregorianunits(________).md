---
title: 'CFAbsoluteTimeGetDifferenceAsGregorianUnits(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfabsolutetimegetdifferenceasgregorianunits(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfabsolutetimegetdifferenceasgregorianunits(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfabsolutetimegetdifferenceasgregorianunits%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2fe8c8f2cafb55bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAbsoluteTimeGetDifferenceAsGregorianUnits(_:_:_:_:)

<sub>Function</sub>

Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units.

> [!warning] Deprecated
> Use CFCalendar or NSCalendar API instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAbsoluteTimeGetDifferenceAsGregorianUnits(_ at1: CFAbsoluteTime, _ at2: CFAbsoluteTime, _ tz: CFTimeZone!, _ unitFlags: CFOptionFlags) -> CFGregorianUnits
```

## Parameters

- `at1` — An absolute time.

- `at2` — An absolute time.

- `tz` — The time zone to use for time correction. Pass `NULL` for GMT.

- `unitFlags` — A mask that specifies which Gregorian unit fields to use when converting the absolute time difference into a Gregorian interval. See [CFGregorianUnitFlags](cfgregorianunitflags.md) for a list of values from which to construct the mask.

## Return Value

The difference between the specified absolute times (as `at1 - at2`—if `at1` is earlier than `at2`, the result is negative) expressed in the units specified by `unitFlags`.

## Discussion

The temporal difference is expressed as accurately as possible, given the units specified. For example, if you asked for the number of months and hours between 2:30pm on April 8 2005 and 5:45pm September 9 2005, the result would be 5 months and 27 hours.

The following example prints the number of hours and minutes between the current time (now) and the reference date (1 January 2001 00:00:00 GMT).

```objc
CFAbsoluteTime now = CFAbsoluteTimeGetCurrent ();
 
CFGregorianUnits units = CFAbsoluteTimeGetDifferenceAsGregorianUnits
    (now, 0, NULL, (kCFGregorianUnitsHours | kCFGregorianUnitsMinutes));
 
CFStringRef output = CFStringCreateWithFormat
    (NULL, 0, CFSTR("hours: %d; minutes: %d"), units.hours, units.minutes);
CFShow(output);
```

## See Also

### Core Foundation Time Utilities Miscellaneous Functions

- [CFAbsoluteTimeAddGregorianUnits](<cfabsolutetimeaddgregorianunits(______).md>) — Adds a time interval, expressed as Gregorian units, to a given absolute time. _(deprecated)_
- [CFAbsoluteTimeGetCurrent](<cfabsolutetimegetcurrent().md>) — Returns the current system absolute time.
- [CFAbsoluteTimeGetDayOfWeek](<cfabsolutetimegetdayofweek(____).md>) — Returns an integer representing the day of the week indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDayOfYear](<cfabsolutetimegetdayofyear(____).md>) — Returns an integer representing the day of the year indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetGregorianDate](<cfabsolutetimegetgregoriandate(____).md>) — Converts an absolute time value into a Gregorian date. _(deprecated)_
- [CFAbsoluteTimeGetWeekOfYear](<cfabsolutetimegetweekofyear(____).md>) — Returns an integer representing the week of the year indicated by the specified absolute time. _(deprecated)_
- [CFGregorianDateGetAbsoluteTime](<cfgregoriandategetabsolutetime(____).md>) — Converts a Gregorian date value into an absolute time value. _(deprecated)_
- [CFGregorianDateIsValid](<cfgregoriandateisvalid(____).md>) — Checks the specified fields of a CFGregorianDate structure for valid values. _(deprecated)_

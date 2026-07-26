---
title: 'CFAbsoluteTimeGetGregorianDate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfabsolutetimegetgregoriandate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfabsolutetimegetgregoriandate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfabsolutetimegetgregoriandate%28_%3A_%3A%29.json'
content_hash: 'sha256:09aea76fca84a622'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAbsoluteTimeGetGregorianDate(_:_:)

<sub>Function</sub>

Converts an absolute time value into a Gregorian date.

> [!warning] Deprecated
> Use CFCalendar or NSCalendar API instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAbsoluteTimeGetGregorianDate(_ at: CFAbsoluteTime, _ tz: CFTimeZone!) -> CFGregorianDate
```

## Parameters

- `at` — The absolute time value to convert.

- `tz` — The time zone to use for time correction. Pass `NULL` for GMT.

## Return Value

The Gregorian date equivalent for `at`.

## See Also

### Core Foundation Time Utilities Miscellaneous Functions

- [CFAbsoluteTimeAddGregorianUnits](<cfabsolutetimeaddgregorianunits(______).md>) — Adds a time interval, expressed as Gregorian units, to a given absolute time. _(deprecated)_
- [CFAbsoluteTimeGetCurrent](<cfabsolutetimegetcurrent().md>) — Returns the current system absolute time.
- [CFAbsoluteTimeGetDayOfWeek](<cfabsolutetimegetdayofweek(____).md>) — Returns an integer representing the day of the week indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDayOfYear](<cfabsolutetimegetdayofyear(____).md>) — Returns an integer representing the day of the year indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDifferenceAsGregorianUnits](<cfabsolutetimegetdifferenceasgregorianunits(________).md>) — Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units. _(deprecated)_
- [CFAbsoluteTimeGetWeekOfYear](<cfabsolutetimegetweekofyear(____).md>) — Returns an integer representing the week of the year indicated by the specified absolute time. _(deprecated)_
- [CFGregorianDateGetAbsoluteTime](<cfgregoriandategetabsolutetime(____).md>) — Converts a Gregorian date value into an absolute time value. _(deprecated)_
- [CFGregorianDateIsValid](<cfgregoriandateisvalid(____).md>) — Checks the specified fields of a CFGregorianDate structure for valid values. _(deprecated)_

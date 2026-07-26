---
title: CFAbsoluteTimeGetCurrent()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfabsolutetimegetcurrent()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfabsolutetimegetcurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfabsolutetimegetcurrent%28%29.json'
content_hash: 'sha256:0f5c9bff7d0d97fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAbsoluteTimeGetCurrent()

<sub>Function</sub>

Returns the current system absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAbsoluteTimeGetCurrent() -> CFAbsoluteTime
```

## Return Value

The current absolute time.

## Discussion

Absolute time is measured in seconds relative to the absolute reference date of Jan 1 2001 00:00:00 GMT. A positive value represents a date after the reference date, a negative value represents a date before it. For example, the absolute time `-32940326` is equivalent to December 16th, 1999 at 17:54:34. Repeated calls to this function do not guarantee monotonically increasing results. The system time may decrease due to synchronization with external time references or due to an explicit user change of the clock.

## See Also

### Core Foundation Time Utilities Miscellaneous Functions

- [CFAbsoluteTimeAddGregorianUnits](<cfabsolutetimeaddgregorianunits(______).md>) — Adds a time interval, expressed as Gregorian units, to a given absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDayOfWeek](<cfabsolutetimegetdayofweek(____).md>) — Returns an integer representing the day of the week indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDayOfYear](<cfabsolutetimegetdayofyear(____).md>) — Returns an integer representing the day of the year indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDifferenceAsGregorianUnits](<cfabsolutetimegetdifferenceasgregorianunits(________).md>) — Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units. _(deprecated)_
- [CFAbsoluteTimeGetGregorianDate](<cfabsolutetimegetgregoriandate(____).md>) — Converts an absolute time value into a Gregorian date. _(deprecated)_
- [CFAbsoluteTimeGetWeekOfYear](<cfabsolutetimegetweekofyear(____).md>) — Returns an integer representing the week of the year indicated by the specified absolute time. _(deprecated)_
- [CFGregorianDateGetAbsoluteTime](<cfgregoriandategetabsolutetime(____).md>) — Converts a Gregorian date value into an absolute time value. _(deprecated)_
- [CFGregorianDateIsValid](<cfgregoriandateisvalid(____).md>) — Checks the specified fields of a CFGregorianDate structure for valid values. _(deprecated)_

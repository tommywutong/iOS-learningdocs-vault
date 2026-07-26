---
title: Time Utilities
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/time-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/time-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/time-utilities.json'
content_hash: 'sha256:ab1179755f4bffa5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# Time Utilities

<sub>API Collection</sub>

## Overview

Core Foundation measures time in units of seconds. The base data type is the [CFTimeInterval](cftimeinterval.md), which measures the difference in seconds between two times. Fixed times, or dates, are defined by the [CFAbsoluteTime](cfabsolutetime.md) data type, which measures the time interval between a particular date and the absolute reference date of Jan 1 2001 00:00:00 GMT.

The [CFGregorianDate](cfgregoriandate.md) structure represents absolute times in terms of the Gregorian calendar. Functions such as [CFAbsoluteTimeGetGregorianDate](<cfabsolutetimegetgregoriandate(____).md>) use a [CFTimeZone](cftimezone.md) object to obtain the local time in a particular time zone.

The [CFDate](cfdate.md) opaque type wraps an absolute time into a [CFTypeRef](cftyperef.md)-base object, allowing you to put time objects into collections and property lists and to be handled by other object-oriented parts of Core Foundation.

## Topics

### Core Foundation Time Utilities Miscellaneous Functions

- [CFAbsoluteTimeAddGregorianUnits](<cfabsolutetimeaddgregorianunits(______).md>) — Adds a time interval, expressed as Gregorian units, to a given absolute time. _(deprecated)_
- [CFAbsoluteTimeGetCurrent](<cfabsolutetimegetcurrent().md>) — Returns the current system absolute time.
- [CFAbsoluteTimeGetDayOfWeek](<cfabsolutetimegetdayofweek(____).md>) — Returns an integer representing the day of the week indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDayOfYear](<cfabsolutetimegetdayofyear(____).md>) — Returns an integer representing the day of the year indicated by the specified absolute time. _(deprecated)_
- [CFAbsoluteTimeGetDifferenceAsGregorianUnits](<cfabsolutetimegetdifferenceasgregorianunits(________).md>) — Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units. _(deprecated)_
- [CFAbsoluteTimeGetGregorianDate](<cfabsolutetimegetgregoriandate(____).md>) — Converts an absolute time value into a Gregorian date. _(deprecated)_
- [CFAbsoluteTimeGetWeekOfYear](<cfabsolutetimegetweekofyear(____).md>) — Returns an integer representing the week of the year indicated by the specified absolute time. _(deprecated)_
- [CFGregorianDateGetAbsoluteTime](<cfgregoriandategetabsolutetime(____).md>) — Converts a Gregorian date value into an absolute time value. _(deprecated)_
- [CFGregorianDateIsValid](<cfgregoriandateisvalid(____).md>) — Checks the specified fields of a CFGregorianDate structure for valid values. _(deprecated)_

### Data Types

- [CFAbsoluteTime](cfabsolutetime.md) — Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [CFGregorianDate](cfgregoriandate.md) — Structure used to represent a point in time using the Gregorian calendar. _(deprecated)_
- [CFGregorianUnits](cfgregorianunits.md) — Structure used to represent a time interval in Gregorian units. _(deprecated)_
- [CFTimeInterval](cftimeinterval.md) — Type used to represent elapsed time in seconds.

### Constants

- [CFGregorianUnitFlags](cfgregorianunitflags.md) — These option flags are used as a mask to indicate a specific set of fields in the CFGregorianDate or CFGregorianUnits structures.
- [Predefined Time Interval Values](predefined-time-interval-values.md) — Time intervals between the absolute reference date and certain other dates.

## See Also

### Related Documentation

- [Date and Time Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)

### Utilities

- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)

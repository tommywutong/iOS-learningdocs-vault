---
title: NSWrapCalendarComponents
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswrapcalendarcomponents-api
source_url: 'https://developer.apple.com/documentation/foundation/nswrapcalendarcomponents-api'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswrapcalendarcomponents-api.json'
content_hash: 'sha256:344a7635ad49e60a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Dates and Times](dates-and-times.md) · [NSCalendar](nscalendar.md)

# NSWrapCalendarComponents

<sub>API Collection</sub>

A legacy constant used to control overflow in date calculations.

## Overview

> [!warning] Deprecated
> Use [NSCalendarWrapComponents](nscalendar/options/wrapcomponents.md) instead.

## Topics

### Constants

- [NSWrapCalendarComponents](nswrapcalendarcomponents.md) — Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented. _(deprecated)_

## See Also

### Scanning Dates

- [- startOfDayForDate:](<nscalendar/startofday(for_).md>) — Returns the first moment of a given date as a date instance.
- [- enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:](<nscalendar/enumeratedates(startingafter_matching_options_using_).md>) — Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [- nextDateAfterDate:matchingComponents:options:](<nscalendar/nextdate(after_matching_options_).md>) — Returns the next date after a given date matching the given components.
- [- nextDateAfterDate:matchingHour:minute:second:options:](<nscalendar/nextdate(after_matchinghour_minute_second_options_).md>) — Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [- nextDateAfterDate:matchingUnit:value:options:](<nscalendar/nextdate(after_matching_value_options_).md>) — Returns the next date after a given date matching the given calendar unit value.
- [Options](nscalendar/options.md) — The options for arithmetic operations involving calendars.

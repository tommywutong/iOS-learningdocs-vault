---
title: 'nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/nextdate%28after%3Amatching%3Amatchingpolicy%3Arepeatedtimepolicy%3Adirection%3A%29.json'
content_hash: 'sha256:927d549dd8711813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)

<sub>Instance Method</sub>

Computes the next date which matches (or most closely matches) a given set of components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextDate(after date: Date, matching components: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward) -> Date?
```

## Parameters

- `date` — The starting date.

- `components` — The components to search for.

- `matchingPolicy` — Specifies the technique the search algorithm uses to find results. Default value is `.nextTime`.

- `repeatedTimePolicy` — Specifies the behavior when multiple matches are found. Default value is `.first`.

- `direction` — Specifies the direction in time to search. Default is `.forward`.

## Return Value

A `Date` representing the result of the search, or `nil` if a result could not be found.

## Discussion

The general semantics follow those of the `enumerateDates` function. To compute a sequence of results, use the `enumerateDates` function, rather than looping and calling this method with the previous loop iteration’s result.

## See Also

### Scanning Dates

- [startOfDay(for:)](<startofday(for_).md>) — Returns the first moment of a given Date, as a Date.
- [enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)](<enumeratedates(startingafter_matching_matchingpolicy_repeatedtimepolicy_direction_using_).md>) — Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [MatchingPolicy](matchingpolicy.md) — A hint to the search algorithm to control the method used for searching for dates.
- [RepeatedTimePolicy](repeatedtimepolicy.md) — Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

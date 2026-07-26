---
title: 'startOfDay(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/calendar/startofday(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/calendar/startofday(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/startofday%28for%3A%29.json'
content_hash: 'sha256:5b380604cab2ec6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# startOfDay(for:)

<sub>Instance Method</sub>

Returns the first moment of a given Date, as a Date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startOfDay(for date: Date) -> Date
```

## Parameters

- `date` — The date to search.

## Return Value

The first moment of the given date.

## Discussion

For example, pass in `Date()`, if you want the start of today. If there were two midnights, it returns the first.  If there was none, it returns the first moment that did exist.

## See Also

### Scanning Dates

- [enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)](<enumeratedates(startingafter_matching_matchingpolicy_repeatedtimepolicy_direction_using_).md>) — Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)](<nextdate(after_matching_matchingpolicy_repeatedtimepolicy_direction_).md>) — Computes the next date which matches (or most closely matches) a given set of components.
- [MatchingPolicy](matchingpolicy.md) — A hint to the search algorithm to control the method used for searching for dates.
- [RepeatedTimePolicy](repeatedtimepolicy.md) — Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

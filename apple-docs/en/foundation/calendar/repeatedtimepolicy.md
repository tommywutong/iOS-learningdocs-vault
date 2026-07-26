---
title: Calendar.RepeatedTimePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/repeatedtimepolicy
source_url: 'https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/repeatedtimepolicy.json'
content_hash: 'sha256:4e5adf103cf69378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# Calendar.RepeatedTimePolicy

<sub>Enumeration</sub>

Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RepeatedTimePolicy
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [Calendar.RepeatedTimePolicy.first](repeatedtimepolicy/first.md) — If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.
- [Calendar.RepeatedTimePolicy.last](repeatedtimepolicy/last.md) — If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

## See Also

### Scanning Dates

- [startOfDay(for:)](<startofday(for_).md>) — Returns the first moment of a given Date, as a Date.
- [enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)](<enumeratedates(startingafter_matching_matchingpolicy_repeatedtimepolicy_direction_using_).md>) — Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)](<nextdate(after_matching_matchingpolicy_repeatedtimepolicy_direction_).md>) — Computes the next date which matches (or most closely matches) a given set of components.
- [MatchingPolicy](matchingpolicy.md) — A hint to the search algorithm to control the method used for searching for dates.

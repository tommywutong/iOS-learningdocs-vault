---
title: Calendar.MatchingPolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/matchingpolicy
source_url: 'https://developer.apple.com/documentation/foundation/calendar/matchingpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/matchingpolicy.json'
content_hash: 'sha256:6015866cdb86acec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# Calendar.MatchingPolicy

<sub>Enumeration</sub>

A hint to the search algorithm to control the method used for searching for dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MatchingPolicy
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [Calendar.MatchingPolicy.nextTime](matchingpolicy/nexttime.md) — If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.
- [Calendar.MatchingPolicy.nextTimePreservingSmallerComponents](matchingpolicy/nexttimepreservingsmallercomponents.md) — If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](matchingpolicy/previoustimepreservingsmallercomponents.md) — If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.
- [Calendar.MatchingPolicy.strict](matchingpolicy/strict.md) — If specified, the algorithm travels as far forward or backward as necessary looking for a match.

## See Also

### Scanning Dates

- [startOfDay(for:)](<startofday(for_).md>) — Returns the first moment of a given Date, as a Date.
- [enumerateDates(startingAfter:matching:matchingPolicy:repeatedTimePolicy:direction:using:)](<enumeratedates(startingafter_matching_matchingpolicy_repeatedtimepolicy_direction_using_).md>) — Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [nextDate(after:matching:matchingPolicy:repeatedTimePolicy:direction:)](<nextdate(after_matching_matchingpolicy_repeatedtimepolicy_direction_).md>) — Computes the next date which matches (or most closely matches) a given set of components.
- [RepeatedTimePolicy](repeatedtimepolicy.md) — Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).

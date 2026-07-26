---
title: Calendar.SearchDirection
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/searchdirection
source_url: 'https://developer.apple.com/documentation/foundation/calendar/searchdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/searchdirection.json'
content_hash: 'sha256:ea98499df1633020'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Calendar](../calendar.md)

# Calendar.SearchDirection

<sub>Enumeration</sub>

The direction in time to search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SearchDirection
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [Calendar.SearchDirection.backward](searchdirection/backward.md) — Search for a date earlier in time than the start date.
- [Calendar.SearchDirection.forward](searchdirection/forward.md) — Search for a date later in time than the start date.

## See Also

### Calculating Intervals

- [dateInterval(of:for:)](<dateinterval(of_for_).md>) — Returns the starting time and duration of a given calendar component that contains a given date.
- [dateInterval(of:start:interval:for:)](<dateinterval(of_start_interval_for_).md>) — Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [dateIntervalOfWeekend(containing:)](<dateintervalofweekend(containing_).md>) — Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [dateIntervalOfWeekend(containing:start:interval:)](<dateintervalofweekend(containing_start_interval_).md>) — Find the range of the weekend around the given date, returned via two by-reference parameters.
- [nextWeekend(startingAfter:direction:)](<nextweekend(startingafter_direction_).md>) — Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [nextWeekend(startingAfter:start:interval:direction:)](<nextweekend(startingafter_start_interval_direction_).md>) — Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.

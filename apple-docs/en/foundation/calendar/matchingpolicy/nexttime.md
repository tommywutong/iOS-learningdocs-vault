---
title: Calendar.MatchingPolicy.nextTime
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/matchingpolicy/nexttime
source_url: 'https://developer.apple.com/documentation/foundation/calendar/matchingpolicy/nexttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/matchingpolicy/nexttime.json'
content_hash: 'sha256:4c41442a81830756'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [MatchingPolicy](../matchingpolicy.md)

# Calendar.MatchingPolicy.nextTime

<sub>Case</sub>

If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case nextTime
```

## Discussion

For example, during a daylight saving transition there may be no 2:37am. The result would then be 3:00am, if that does exist.

## See Also

### Enumeration Cases

- [Calendar.MatchingPolicy.nextTimePreservingSmallerComponents](nexttimepreservingsmallercomponents.md) — If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](previoustimepreservingsmallercomponents.md) — If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.
- [Calendar.MatchingPolicy.strict](strict.md) — If specified, the algorithm travels as far forward or backward as necessary looking for a match.

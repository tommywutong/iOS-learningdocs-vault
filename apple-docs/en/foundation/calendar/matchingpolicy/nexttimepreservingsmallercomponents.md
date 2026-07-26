---
title: Calendar.MatchingPolicy.nextTimePreservingSmallerComponents
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/matchingpolicy/nexttimepreservingsmallercomponents
source_url: 'https://developer.apple.com/documentation/foundation/calendar/matchingpolicy/nexttimepreservingsmallercomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/matchingpolicy/nexttimepreservingsmallercomponents.json'
content_hash: 'sha256:5effd6c580e23015'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [MatchingPolicy](../matchingpolicy.md)

# Calendar.MatchingPolicy.nextTimePreservingSmallerComponents

<sub>Case</sub>

If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case nextTimePreservingSmallerComponents
```

## See Also

### Enumeration Cases

- [Calendar.MatchingPolicy.nextTime](nexttime.md) — If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](previoustimepreservingsmallercomponents.md) — If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.
- [Calendar.MatchingPolicy.strict](strict.md) — If specified, the algorithm travels as far forward or backward as necessary looking for a match.

---
title: Calendar.RepeatedTimePolicy.first
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/repeatedtimepolicy/first
source_url: 'https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy/first'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/repeatedtimepolicy/first.json'
content_hash: 'sha256:bb088bd4be2f695e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RepeatedTimePolicy](../repeatedtimepolicy.md)

# Calendar.RepeatedTimePolicy.first

<sub>Case</sub>

If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case first
```

## See Also

### Enumeration Cases

- [Calendar.RepeatedTimePolicy.last](last.md) — If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

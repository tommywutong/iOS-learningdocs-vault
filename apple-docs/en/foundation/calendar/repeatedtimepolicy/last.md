---
title: Calendar.RepeatedTimePolicy.last
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/calendar/repeatedtimepolicy/last
source_url: 'https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy/last'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/calendar/repeatedtimepolicy/last.json'
content_hash: 'sha256:0159de4a212791bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Calendar](../../calendar.md) · [RepeatedTimePolicy](../repeatedtimepolicy.md)

# Calendar.RepeatedTimePolicy.last

<sub>Case</sub>

If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case last
```

## See Also

### Enumeration Cases

- [Calendar.RepeatedTimePolicy.first](first.md) — If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.

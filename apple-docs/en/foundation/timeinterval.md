---
title: TimeInterval
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timeinterval
source_url: 'https://developer.apple.com/documentation/foundation/timeinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timeinterval.json'
content_hash: 'sha256:f92d3c79746018b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# TimeInterval

<sub>Type Alias</sub>

A number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias TimeInterval = Double
```

## Discussion

A [TimeInterval](timeinterval.md) value is always specified in seconds; it yields sub-millisecond precision over a range of 10,000 years.

On its own, a time interval does not specify a unique point in time, or even a span between specific times. Combining a time interval with one or more known reference points yields a [Date](date.md) or [DateInterval](dateinterval.md) value.

## See Also

### Date Representations

- [Date](date.md) — A specific point in time, independent of any calendar or time zone.
- [DateInterval](dateinterval.md) — The span of time between a specific start date and end date.

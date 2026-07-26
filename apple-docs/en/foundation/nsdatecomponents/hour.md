---
title: hour
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/hour
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/hour'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/hour.json'
content_hash: 'sha256:d8d9bdac024d2cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# hour

<sub>Instance Property</sub>

The number of hour units for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hour: Int { get set }
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Hours and Seconds

- [minute](minute.md) — The number of minute units for the receiver.
- [second](second.md) — The number of second units for the receiver.
- [nanosecond](nanosecond.md) — The number of nanosecond units for the receiver.

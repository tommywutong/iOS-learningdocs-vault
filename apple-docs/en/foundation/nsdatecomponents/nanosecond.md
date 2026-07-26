---
title: nanosecond
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdatecomponents/nanosecond
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/nanosecond'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/nanosecond.json'
content_hash: 'sha256:a912f01cbc49ac00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# nanosecond

<sub>Instance Property</sub>

The number of nanosecond units for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nanosecond: Int { get set }
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Hours and Seconds

- [hour](hour.md) — The number of hour units for the receiver.
- [minute](minute.md) — The number of minute units for the receiver.
- [second](second.md) — The number of second units for the receiver.

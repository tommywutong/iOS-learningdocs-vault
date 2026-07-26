---
title: timeIntervalSinceNow
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/timeintervalsincenow
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/timeintervalsincenow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/timeintervalsincenow.json'
content_hash: 'sha256:dcf5dde1cd4ef6a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# timeIntervalSinceNow

<sub>Instance Property</sub>

The interval between the date object and the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeIntervalSinceNow: TimeInterval { get }
```

## Discussion

If the date object is earlier than the current date and time, this property’s value is negative.

## See Also

### Getting Time Intervals

- [- timeIntervalSinceDate:](<timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
- [timeIntervalSinceReferenceDate](timeintervalsincereferencedate-swift.property.md) — The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSince1970](timeintervalsince1970.md) — The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [timeIntervalSinceReferenceDate](timeintervalsincereferencedate-swift.type.property.md) — The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [NSTimeIntervalSince1970](../nstimeintervalsince1970.md) — The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

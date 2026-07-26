---
title: timeIntervalSince1970
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/timeintervalsince1970
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/timeintervalsince1970'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/timeintervalsince1970.json'
content_hash: 'sha256:0d45f43af15b8f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# timeIntervalSince1970

<sub>Instance Property</sub>

The interval between the date object and 00:00:00 UTC on 1 January 1970.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeIntervalSince1970: TimeInterval { get }
```

## Discussion

This property’s value is negative if the date object is earlier than 00:00:00 UTC on 1 January 1970.

## See Also

### Getting Time Intervals

- [- timeIntervalSinceDate:](<timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
- [timeIntervalSinceNow](timeintervalsincenow.md) — The interval between the date object and the current date and time.
- [timeIntervalSinceReferenceDate](timeintervalsincereferencedate-swift.property.md) — The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSinceReferenceDate](timeintervalsincereferencedate-swift.type.property.md) — The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [NSTimeIntervalSince1970](../nstimeintervalsince1970.md) — The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

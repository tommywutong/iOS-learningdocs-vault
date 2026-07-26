---
title: timeIntervalSinceReferenceDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/timeintervalsincereferencedate-swift.type.property
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/timeintervalsincereferencedate-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/timeintervalsincereferencedate-swift.type.property.json'
content_hash: 'sha256:25fe316fdbfbd127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# timeIntervalSinceReferenceDate

<sub>Type Property</sub>

The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var timeIntervalSinceReferenceDate: TimeInterval { get }
```

## Return Value

The interval between the system’s absolute reference date (00:00:00 UTC on 1 January 2001) and the current date and time.

## Discussion

This method is the primitive method for [NSDate](../nsdate.md). If you subclass [NSDate](../nsdate.md), you must override this method with your own implementation for it.

## See Also

### Getting Time Intervals

- [- timeIntervalSinceDate:](<timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
- [timeIntervalSinceNow](timeintervalsincenow.md) — The interval between the date object and the current date and time.
- [timeIntervalSinceReferenceDate](timeintervalsincereferencedate-swift.property.md) — The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSince1970](timeintervalsince1970.md) — The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [NSTimeIntervalSince1970](../nstimeintervalsince1970.md) — The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

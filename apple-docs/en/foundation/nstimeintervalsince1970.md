---
title: NSTimeIntervalSince1970
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstimeintervalsince1970
source_url: 'https://developer.apple.com/documentation/foundation/nstimeintervalsince1970'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstimeintervalsince1970.json'
content_hash: 'sha256:3d2d70ba51367427'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSTimeIntervalSince1970

<sub>Global Variable</sub>

The number of seconds from 1 January 1970 to the reference date, 1 January 2001.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSTimeIntervalSince1970: Double { get }
```

## Discussion

1 January 1970 is the epoch (or starting point) for Unix time.

## See Also

### Getting Time Intervals

- [- timeIntervalSinceDate:](<nsdate/timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
- [timeIntervalSinceNow](nsdate/timeintervalsincenow.md) — The interval between the date object and the current date and time.
- [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.property.md) — The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [timeIntervalSince1970](nsdate/timeintervalsince1970.md) — The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [timeIntervalSinceReferenceDate](nsdate/timeintervalsincereferencedate-swift.type.property.md) — The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.

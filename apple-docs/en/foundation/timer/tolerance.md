---
title: tolerance
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/tolerance
source_url: 'https://developer.apple.com/documentation/foundation/timer/tolerance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/tolerance.json'
content_hash: 'sha256:e470b3bb8a72def3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# tolerance

<sub>Instance Property</sub>

The amount of time after the scheduled fire date that the timer may fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tolerance: TimeInterval { get set }
```

## Discussion

The default value is zero, which means no additional tolerance is applied.

Setting a tolerance for a timer allows it to fire later than the scheduled fire date. Allowing the system flexibility in when a timer fires increases the ability of the system to optimize for increased power savings and responsiveness.

The timer may fire at any time between its scheduled fire date and the scheduled fire date plus the tolerance. The timer will not fire before the scheduled fire date. For repeating timers, the next fire date is calculated from the original fire date regardless of tolerance applied at individual fire times, to avoid drift. The system reserves the right to apply a small amount of tolerance to certain timers regardless of the value of this property.

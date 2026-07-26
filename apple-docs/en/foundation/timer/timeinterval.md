---
title: timeInterval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/timeinterval
source_url: 'https://developer.apple.com/documentation/foundation/timer/timeinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/timeinterval.json'
content_hash: 'sha256:3cad6f2bb3c7c731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# timeInterval

<sub>Instance Property</sub>

The timer’s time interval, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeInterval: TimeInterval { get }
```

## Discussion

If the timer is non-repeating, returns `0` even if a time interval was set.

## See Also

### Retrieving Timer Information

- [valid](isvalid.md) — A Boolean value that indicates whether the timer is currently valid.
- [fireDate](firedate.md) — The date at which the timer will fire.
- [userInfo](userinfo.md) — The receiver’s `userInfo` object.

---
title: isValid
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/isvalid
source_url: 'https://developer.apple.com/documentation/foundation/timer/isvalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/isvalid.json'
content_hash: 'sha256:4c1efd05fe209b21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# isValid

<sub>Instance Property</sub>

A Boolean value that indicates whether the timer is currently valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isValid: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver is still capable of firing or [false](../../swift/false.md) if the timer has been invalidated and is no longer capable of firing.

## See Also

### Retrieving Timer Information

- [fireDate](firedate.md) — The date at which the timer will fire.
- [timeInterval](timeinterval.md) — The timer’s time interval, in seconds.
- [userInfo](userinfo.md) — The receiver’s `userInfo` object.

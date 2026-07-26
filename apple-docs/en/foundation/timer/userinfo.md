---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/timer/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/userinfo.json'
content_hash: 'sha256:f478f44433af79cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# userInfo

<sub>Instance Property</sub>

The receiver’s `userInfo` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: Any? { get }
```

## Discussion

Do not access this property after the timer is invalidated. Use [valid](isvalid.md) to test whether the timer is valid.

## See Also

### Related Documentation

- [+ timerWithTimeInterval:target:selector:userInfo:repeats:](<init(timeinterval_target_selector_userinfo_repeats_).md>) — Initializes a timer object with the specified object and selector.
- [+ scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](<scheduledtimer(timeinterval_target_selector_userinfo_repeats_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [- invalidate](<invalidate().md>) — Stops the timer from ever firing again and requests its removal from its run loop.

### Retrieving Timer Information

- [valid](isvalid.md) — A Boolean value that indicates whether the timer is currently valid.
- [fireDate](firedate.md) — The date at which the timer will fire.
- [timeInterval](timeinterval.md) — The timer’s time interval, in seconds.

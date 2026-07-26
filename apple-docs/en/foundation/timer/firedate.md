---
title: fireDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/timer/firedate
source_url: 'https://developer.apple.com/documentation/foundation/timer/firedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/firedate.json'
content_hash: 'sha256:eebbda37cc4dbf15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# fireDate

<sub>Instance Property</sub>

The date at which the timer will fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fireDate: Date { get set }
```

## Discussion

If the timer is no longer valid, the last date at which the timer fired.

You can set this property to adjust the firing time of a repeating timer. Although resetting a timer’s next firing time is a relatively expensive operation, it may be more efficient in some situations. For example, you could use it in situations where you want to repeat an action multiple times in the future, but at irregular time intervals. Adjusting the firing time of a single timer would likely incur less expense than creating multiple timer objects, scheduling each one on a run loop, and then destroying them.

You should not change the fire date of a timer that has been invalidated, which includes non-repeating timers that have already fired. You could potentially change the fire date of a non-repeating timer that had not yet fired, although you should always do so from the thread to which the timer is attached to avoid potential race conditions.

Use the [valid](isvalid.md) method to verify that the timer is valid.

## See Also

### Retrieving Timer Information

- [valid](isvalid.md) — A Boolean value that indicates whether the timer is currently valid.
- [timeInterval](timeinterval.md) — The timer’s time interval, in seconds.
- [userInfo](userinfo.md) — The receiver’s `userInfo` object.

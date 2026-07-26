---
title: 'scheduledTimer(timeInterval:invocation:repeats:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/scheduledtimer(timeinterval:invocation:repeats:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/scheduledtimer(timeinterval:invocation:repeats:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/scheduledtimer%28timeinterval%3Ainvocation%3Arepeats%3A%29.json'
content_hash: 'sha256:799169a6b3985c04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# scheduledTimer(timeInterval:invocation:repeats:)

<sub>Type Method</sub>

Creates a new timer and schedules it on the current run loop in the default mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func scheduledTimer(timeInterval ti: TimeInterval, invocation: NSInvocation, repeats yesOrNo: Bool) -> Timer
```

## Parameters

- `ti` — The number of seconds between firings of the timer. If `ti` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.

- `invocation` — The invocation to use when the timer fires. The invocation object maintains a strong reference to its arguments until the timer is invalidated.

- `yesOrNo` — If [true](../../swift/true.md), the timer will repeatedly reschedule itself until invalidated. If [false](../../swift/false.md), the timer will be invalidated after it fires.

## Return Value

A new `NSTimer` object, configured according to the specified parameters.

## Discussion

After `ti` seconds have elapsed, the timer fires, invoking `invocation`.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Timer Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Timers/Timers.html#//apple_ref/doc/uid/10000061i)

### Creating a Timer

- [+ scheduledTimerWithTimeInterval:repeats:block:](<scheduledtimer(withtimeinterval_repeats_block_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](<scheduledtimer(timeinterval_target_selector_userinfo_repeats_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ timerWithTimeInterval:repeats:block:](<init(timeinterval_repeats_block_).md>) — Initializes a timer object with the specified time interval and block.
- [+ timerWithTimeInterval:target:selector:userInfo:repeats:](<init(timeinterval_target_selector_userinfo_repeats_).md>) — Initializes a timer object with the specified object and selector.
- [+ timerWithTimeInterval:invocation:repeats:](<init(timeinterval_invocation_repeats_).md>) — Initializes a timer object with the specified invocation object.
- [- initWithFireDate:interval:repeats:block:](<init(fire_interval_repeats_block_).md>) — Initializes a timer for the specified date and time interval with the specified block.
- [- initWithFireDate:interval:target:selector:userInfo:repeats:](<init(fireat_interval_target_selector_userinfo_repeats_).md>) — Initializes a timer using the specified object and selector.

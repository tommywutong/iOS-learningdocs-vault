---
title: 'scheduledTimer(withTimeInterval:repeats:block:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/scheduledtimer(withtimeinterval:repeats:block:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/scheduledtimer(withtimeinterval:repeats:block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/scheduledtimer%28withtimeinterval%3Arepeats%3Ablock%3A%29.json'
content_hash: 'sha256:d3118fcfdd2a72d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# scheduledTimer(withTimeInterval:repeats:block:)

<sub>Type Method</sub>

Creates a timer and schedules it on the current run loop in the default mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func scheduledTimer(withTimeInterval interval: TimeInterval, repeats: Bool, block: @escaping @Sendable (Timer) -> Void) -> Timer
```

## Parameters

- `interval` — The number of seconds between firings of the timer. If `interval` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.

- `repeats` — If `true`, the timer will repeatedly reschedule itself until invalidated. If `false`, the timer will be invalidated after it fires.

- `block` — A block to be executed when the timer fires. The block takes a single `NSTimer` parameter and has no return value.

## Return Value

A new `NSTimer` object, configured according to the specified parameters.

## Discussion

After `interval` seconds have elapsed, the timer fires, executing `block`.

## See Also

### Creating a Timer

- [+ scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](<scheduledtimer(timeinterval_target_selector_userinfo_repeats_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:invocation:repeats:](<scheduledtimer(timeinterval_invocation_repeats_).md>) — Creates a new timer and schedules it on the current run loop in the default mode.
- [+ timerWithTimeInterval:repeats:block:](<init(timeinterval_repeats_block_).md>) — Initializes a timer object with the specified time interval and block.
- [+ timerWithTimeInterval:target:selector:userInfo:repeats:](<init(timeinterval_target_selector_userinfo_repeats_).md>) — Initializes a timer object with the specified object and selector.
- [+ timerWithTimeInterval:invocation:repeats:](<init(timeinterval_invocation_repeats_).md>) — Initializes a timer object with the specified invocation object.
- [- initWithFireDate:interval:repeats:block:](<init(fire_interval_repeats_block_).md>) — Initializes a timer for the specified date and time interval with the specified block.
- [- initWithFireDate:interval:target:selector:userInfo:repeats:](<init(fireat_interval_target_selector_userinfo_repeats_).md>) — Initializes a timer using the specified object and selector.

---
title: 'init(timeInterval:repeats:block:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/init(timeinterval:repeats:block:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/init(timeinterval:repeats:block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/init%28timeinterval%3Arepeats%3Ablock%3A%29.json'
content_hash: 'sha256:3bb282009fb76e75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# init(timeInterval:repeats:block:)

<sub>Initializer</sub>

Initializes a timer object with the specified time interval and block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timeInterval interval: TimeInterval, repeats: Bool, block: @escaping @Sendable (Timer) -> Void)
```

## Parameters

- `interval` — The number of seconds between firings of the timer. If `interval` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.

- `repeats` — If `true`, the timer will repeatedly reschedule itself until invalidated. If `false`, the timer will be invalidated after it fires.

- `block` — A block to be executed when the timer fires. The block takes a single [Timer](../timer.md) parameter and has no return value.

## Return Value

A new [Timer](../timer.md) object, configured according to the specified parameters.

## Discussion

You must add the new timer to a run loop, using [- addTimer:forMode:](<../runloop/add(__formode_)-392ag.md>). Then, after `interval` seconds have elapsed, the timer fires, executing `block`. (If the timer is configured to repeat, you don’t need to add the timer to the run loop again.)

## See Also

### Creating a Timer

- [+ scheduledTimerWithTimeInterval:repeats:block:](<scheduledtimer(withtimeinterval_repeats_block_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](<scheduledtimer(timeinterval_target_selector_userinfo_repeats_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:invocation:repeats:](<scheduledtimer(timeinterval_invocation_repeats_).md>) — Creates a new timer and schedules it on the current run loop in the default mode.
- [+ timerWithTimeInterval:target:selector:userInfo:repeats:](<init(timeinterval_target_selector_userinfo_repeats_).md>) — Initializes a timer object with the specified object and selector.
- [+ timerWithTimeInterval:invocation:repeats:](<init(timeinterval_invocation_repeats_).md>) — Initializes a timer object with the specified invocation object.
- [- initWithFireDate:interval:repeats:block:](<init(fire_interval_repeats_block_).md>) — Initializes a timer for the specified date and time interval with the specified block.
- [- initWithFireDate:interval:target:selector:userInfo:repeats:](<init(fireat_interval_target_selector_userinfo_repeats_).md>) — Initializes a timer using the specified object and selector.

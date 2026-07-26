---
title: 'init(fire:interval:repeats:block:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/init(fire:interval:repeats:block:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/init(fire:interval:repeats:block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/init%28fire%3Ainterval%3Arepeats%3Ablock%3A%29.json'
content_hash: 'sha256:d2681ab83316c715'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# init(fire:interval:repeats:block:)

<sub>Initializer</sub>

Initializes a timer for the specified date and time interval with the specified block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fire date: Date, interval: TimeInterval, repeats: Bool, block: @escaping @Sendable (Timer) -> Void)
```

## Parameters

- `date` — The time at which the timer should first fire.

- `interval` — For a repeating timer, this parameter contains the number of seconds between firings of the timer. If `interval` is less than or equal to `0.0`, this method chooses the nonnegative value of `0.0001` seconds instead.

- `repeats` — If [true](../../swift/true.md), the timer will repeatedly reschedule itself until invalidated. If [false](../../swift/false.md), the timer will be invalidated after it fires.

- `block` — A block to be executed when the timer fires. The block takes a single [Timer](../timer.md) parameter and has no return value.

## Return Value

A new [Timer](../timer.md) object, configured according to the specified parameters.

## Discussion

You must add the new timer to a run loop, using [- addTimer:forMode:](<../runloop/add(__formode_)-392ag.md>). Upon firing, after `interval` seconds have elapsed, the timer fires, executing `block`. (If the timer is configured to repeat, you don’t need to add the timer to the run loop again.)

## See Also

### Creating a Timer

- [+ scheduledTimerWithTimeInterval:repeats:block:](<scheduledtimer(withtimeinterval_repeats_block_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](<scheduledtimer(timeinterval_target_selector_userinfo_repeats_).md>) — Creates a timer and schedules it on the current run loop in the default mode.
- [+ scheduledTimerWithTimeInterval:invocation:repeats:](<scheduledtimer(timeinterval_invocation_repeats_).md>) — Creates a new timer and schedules it on the current run loop in the default mode.
- [+ timerWithTimeInterval:repeats:block:](<init(timeinterval_repeats_block_).md>) — Initializes a timer object with the specified time interval and block.
- [+ timerWithTimeInterval:target:selector:userInfo:repeats:](<init(timeinterval_target_selector_userinfo_repeats_).md>) — Initializes a timer object with the specified object and selector.
- [+ timerWithTimeInterval:invocation:repeats:](<init(timeinterval_invocation_repeats_).md>) — Initializes a timer object with the specified invocation object.
- [- initWithFireDate:interval:target:selector:userInfo:repeats:](<init(fireat_interval_target_selector_userinfo_repeats_).md>) — Initializes a timer using the specified object and selector.

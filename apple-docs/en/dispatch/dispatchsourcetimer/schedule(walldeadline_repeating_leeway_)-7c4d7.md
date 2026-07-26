---
title: 'schedule(wallDeadline:repeating:leeway:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-7c4d7'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcetimer/schedule(walldeadline:repeating:leeway:)-7c4d7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcetimer/schedule%28walldeadline%3Arepeating%3Aleeway%3A%29-7c4d7.json'
content_hash: 'sha256:6e57a2229efce862'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceTimer](../dispatchsourcetimer.md)

# schedule(wallDeadline:repeating:leeway:)

<sub>Instance Method</sub>

Schedules a timer with the specified time, repeat interval, and leeway values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(wallDeadline: DispatchWallTime, repeating interval: DispatchTimeInterval = .never, leeway: DispatchTimeInterval = .nanoseconds(0))
```

## Parameters

- `wallDeadline` — The time at which to execute the dispatch source’s event handler.

- `interval` — The repeat interval for the timer, specified as a [DispatchTimeInterval](../dispatchtimeinterval.md) value. Specify [DispatchTimeInterval.never](../dispatchtimeinterval/never.md) if you want the timer to fire only once.

- `leeway` — The maximum amount of time after `wallDeadline` by which the system may delay the delivery of the timer event.

## Discussion

The system may defer the deliver of timer events to improve power consumption and system performance. The first time the timer fires, the maximum allowable delay is equal to the value in the `leeway` parameter. For subsequent firings of a repeating timer, the timer fires at `wallDeadline + (n * repeating)`, and the maximum delay is equal to `min(leeway, repeating/2)`—that is, the smaller of either the `leeway` value or half the value in the `repeating` parameter.

The system may fire a timer sooner than the value in the `wallDeadline` parameter. If you created the timer with the [strict](../dispatchsource/timerflags/strict.md) flag, the system makes every effort to observe the provided `leeway` value, even if it is smaller than the current lower limit.

Calling this method on a cancelled dispatch source has no effect.

## See Also

### Scheduling the Timer Trigger Conditions

- [schedule(deadline:repeating:leeway:)](<schedule(deadline_repeating_leeway_)-hvhp.md>) — Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [schedule(deadline:repeating:leeway:)](<schedule(deadline_repeating_leeway_)-24w9r.md>) — Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [schedule(wallDeadline:repeating:leeway:)](<schedule(walldeadline_repeating_leeway_)-21bay.md>) — Schedules a timer with the specified time, repeat interval, and leeway values.

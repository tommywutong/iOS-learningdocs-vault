---
title: 'scheduleRepeating(deadline:interval:leeway:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift（4.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/dispatch/dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-3k199'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcetimer/schedulerepeating(deadline:interval:leeway:)-3k199'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcetimer/schedulerepeating%28deadline%3Ainterval%3Aleeway%3A%29-3k199.json'
content_hash: 'sha256:022e90a21c91b4bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceTimer](../dispatchsourcetimer.md)

# scheduleRepeating(deadline:interval:leeway:)

<sub>Instance Method</sub>

Schedules a repeating timer with the specified deadline, repeat interval, and leeway values.

> [!warning] Deprecated
> Use [schedule(deadline:repeating:leeway:)](<schedule(deadline_repeating_leeway_)-hvhp.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scheduleRepeating(deadline: DispatchTime, interval: DispatchTimeInterval, leeway: DispatchTimeInterval = .nanoseconds(0))
```

## Parameters

- `deadline` — The Mach absolute time at which to execute the dispatch source’s event handler.

- `interval` — The repeat interval for the timer, specified as a [DispatchTimeInterval](../dispatchtimeinterval.md) value.

- `leeway` — The maximum amount of time after `deadline` by which the system may delay the delivery of the timer event.

## Discussion

The system may defer the deliver of timer events to improve power consumption and system performance. The first time the timer fires, the maximum allowable delay is equal to the value in the `leeway` parameter. For subsequent firings, the timer fires at `deadline + (n * repeating)`, and the maximum delay is equal to `min(leeway, repeating/2)`—that is, the smaller of either the `leeway` value or half the value in the `repeating` parameter.

The system may fire a timer sooner than the value in the `deadline` parameter. If you created the timer with the [strict](../dispatchsource/timerflags/strict.md) flag, the system makes every effort to observe the provided `leeway` value, even if it is smaller than the current lower limit.

Calling this method on a cancelled dispatch source has no effect.

## See Also

### Deprecated

- [scheduleOneshot(deadline:leeway:)](<scheduleoneshot(deadline_leeway_).md>) — Schedules a timer to fire once with the specified deadline and leeway values. _(deprecated)_
- [scheduleOneshot(wallDeadline:leeway:)](<scheduleoneshot(walldeadline_leeway_).md>) — Schedules a timer to fire once with the specified deadline and leeway values. _(deprecated)_
- [scheduleRepeating(deadline:interval:leeway:)](<schedulerepeating(deadline_interval_leeway_)-4wtot.md>) — Schedules a repeating timer with the specified deadline, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<schedulerepeating(walldeadline_interval_leeway_)-6fiox.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<schedulerepeating(walldeadline_interval_leeway_)-942p7.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_

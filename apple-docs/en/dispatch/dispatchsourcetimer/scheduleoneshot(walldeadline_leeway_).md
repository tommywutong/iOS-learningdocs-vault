---
title: 'scheduleOneshot(wallDeadline:leeway:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift（4.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/dispatch/dispatchsourcetimer/scheduleoneshot(walldeadline:leeway:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcetimer/scheduleoneshot(walldeadline:leeway:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcetimer/scheduleoneshot%28walldeadline%3Aleeway%3A%29.json'
content_hash: 'sha256:b4bb9539fef9340b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceTimer](../dispatchsourcetimer.md)

# scheduleOneshot(wallDeadline:leeway:)

<sub>Instance Method</sub>

Schedules a timer to fire once with the specified deadline and leeway values.

> [!warning] Deprecated
> Use [schedule(wallDeadline:repeating:leeway:)](<schedule(walldeadline_repeating_leeway_)-7c4d7.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scheduleOneshot(wallDeadline: DispatchWallTime, leeway: DispatchTimeInterval = .nanoseconds(0))
```

## Parameters

- `wallDeadline` — The time at which to execute the dispatch source’s event handler.

- `leeway` — The maximum amount of time after deadline by which the system may delay the delivery of the timer event.

## Discussion

The system may defer the deliver of timer events to improve power consumption and system performance. The first time the timer fires, the maximum allowable delay is equal to the value in the `leeway` parameter.

The system may fire a timer sooner than the value in the `deadline` parameter. If you created the timer with the [strict](../dispatchsource/timerflags/strict.md) flag, the system makes every effort to observe the provided `leeway` value, even if it is smaller than the current lower limit.

Calling this method on a cancelled dispatch source has no effect.

## See Also

### Deprecated

- [scheduleOneshot(deadline:leeway:)](<scheduleoneshot(deadline_leeway_).md>) — Schedules a timer to fire once with the specified deadline and leeway values. _(deprecated)_
- [scheduleRepeating(deadline:interval:leeway:)](<schedulerepeating(deadline_interval_leeway_)-3k199.md>) — Schedules a repeating timer with the specified deadline, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(deadline:interval:leeway:)](<schedulerepeating(deadline_interval_leeway_)-4wtot.md>) — Schedules a repeating timer with the specified deadline, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<schedulerepeating(walldeadline_interval_leeway_)-6fiox.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<schedulerepeating(walldeadline_interval_leeway_)-942p7.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_

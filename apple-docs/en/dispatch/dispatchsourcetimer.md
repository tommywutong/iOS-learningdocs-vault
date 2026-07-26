---
title: DispatchSourceTimer
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourcetimer
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourcetimer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourcetimer.json'
content_hash: 'sha256:9589e9f2f157af5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceTimer

<sub>Protocol</sub>

A dispatch source that submits the event handler block based on a timer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceTimer : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeTimerSource(flags:queue:)](<dispatchsource/maketimersource(flags_queue_).md>) method to create an object that adopts this protocol.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Scheduling the Timer Trigger Conditions

- [schedule(deadline:repeating:leeway:)](<dispatchsourcetimer/schedule(deadline_repeating_leeway_)-hvhp.md>) — Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [schedule(deadline:repeating:leeway:)](<dispatchsourcetimer/schedule(deadline_repeating_leeway_)-24w9r.md>) — Schedules a timer with the specified deadline, repeat interval, and leeway values.
- [schedule(wallDeadline:repeating:leeway:)](<dispatchsourcetimer/schedule(walldeadline_repeating_leeway_)-7c4d7.md>) — Schedules a timer with the specified time, repeat interval, and leeway values.
- [schedule(wallDeadline:repeating:leeway:)](<dispatchsourcetimer/schedule(walldeadline_repeating_leeway_)-21bay.md>) — Schedules a timer with the specified time, repeat interval, and leeway values.

### Deprecated

- [scheduleOneshot(deadline:leeway:)](<dispatchsourcetimer/scheduleoneshot(deadline_leeway_).md>) — Schedules a timer to fire once with the specified deadline and leeway values. _(deprecated)_
- [scheduleOneshot(wallDeadline:leeway:)](<dispatchsourcetimer/scheduleoneshot(walldeadline_leeway_).md>) — Schedules a timer to fire once with the specified deadline and leeway values. _(deprecated)_
- [scheduleRepeating(deadline:interval:leeway:)](<dispatchsourcetimer/schedulerepeating(deadline_interval_leeway_)-3k199.md>) — Schedules a repeating timer with the specified deadline, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(deadline:interval:leeway:)](<dispatchsourcetimer/schedulerepeating(deadline_interval_leeway_)-4wtot.md>) — Schedules a repeating timer with the specified deadline, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<dispatchsourcetimer/schedulerepeating(walldeadline_interval_leeway_)-6fiox.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_
- [scheduleRepeating(wallDeadline:interval:leeway:)](<dispatchsourcetimer/schedulerepeating(walldeadline_interval_leeway_)-942p7.md>) — Schedules a repeating timer with the specified time, repeat interval, and leeway values. _(deprecated)_

## See Also

### Creating a Timer Source

- [makeTimerSource(flags:queue:)](<dispatchsource/maketimersource(flags_queue_).md>) — Creates a new dispatch source object for monitoring timer events.
- [TimerFlags](dispatchsource/timerflags.md) — Flags to use when configuring a timer dispatch source.

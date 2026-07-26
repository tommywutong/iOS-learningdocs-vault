---
title: Clock
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/clock
source_url: 'https://developer.apple.com/documentation/swift/clock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/clock.json'
content_hash: 'sha256:159b67427b9c7a35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Clock

<sub>Protocol</sub>

A mechanism in which to measure time, and delay work until a given point in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Clock<Duration> : Sendable
```

## Overview

Types that conform to the `Clock` protocol define a concept of “now” which is the specific instant in time that property is accessed. Any pair of calls to the `now` property may have a minimum duration between them - this minimum resolution is exposed by the `minimumResolution` property to inform any user of the type the expected granularity of accuracy.

One of the primary uses for clocks is to schedule task sleeping. This method resumes the calling task after a given deadline has been met or passed with a given tolerance value. The tolerance is expected as a leeway around the deadline. The clock may reschedule tasks within the tolerance to ensure efficient execution of resumptions by reducing potential operating system wake-ups. If no tolerance is specified (i.e. nil is passed in) the sleep function is expected to schedule with a default tolerance strategy.

For more information about specific clocks see `ContinuousClock` and `SuspendingClock`.

## Relationships

- **Inherits From**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

- **Conforming Types**: [ContinuousClock](continuousclock.md), [SuspendingClock](suspendingclock.md)

## Topics

### Associated Types

- [Duration](clock/duration.md)
- [Instant](clock/instant.md)

### Instance Properties

- [minimumResolution](clock/minimumresolution.md)
- [now](clock/now.md)

### Instance Methods

- [measure(_:)](<clock/measure(__)-2emvx.md>) — Measure the elapsed time to execute a closure.
- [measure(_:)](<clock/measure(__)-7l47m.md>) — Measure the elapsed time to execute an asynchronous closure.
- [measure(isolation:_:)](<clock/measure(isolation___).md>) _(deprecated)_
- [sleep(for:tolerance:)](<clock/sleep(for_tolerance_).md>) — Suspends for the given duration.
- [sleep(until:tolerance:)](<clock/sleep(until_tolerance_).md>)

### Type Properties

- [continuous](clock/continuous.md) — A clock that measures time that always increments but does not stop incrementing while the system is asleep.
- [suspending](clock/suspending.md) — A clock that measures time that always increments but stops incrementing while the system is asleep.

## See Also

### Clocks

- [ContinuousClock](continuousclock.md) — A clock that measures time that always increments and does not stop incrementing while the system is asleep.
- [SuspendingClock](suspendingclock.md) — A clock that measures time that always increments but stops incrementing while the system is asleep.

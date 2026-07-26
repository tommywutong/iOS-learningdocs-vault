---
title: SuspendingClock
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/suspendingclock
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock.json'
content_hash: 'sha256:1fa3d8089ba74e2e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SuspendingClock

<sub>Structure</sub>

A clock that measures time that always increments but stops incrementing while the system is asleep.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SuspendingClock
```

## Overview

`SuspendingClock` can be considered as a system awake time clock. The frame of reference of the `Instant` may be bound machine boot or some other locally defined reference point. This means that the instants are only comparable on the same machine in the same booted session.

This clock is suitable for high resolution measurements of execution.

## Relationships

- **Conforms To**: [Clock](clock.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Instant](suspendingclock/instant.md)

### Initializers

- [init()](<suspendingclock/init().md>)

### Instance Properties

- [systemEpoch](suspendingclock/systemepoch.md)

### Type Properties

- [now](suspendingclock/now-swift.type.property.md) — The current instant accounting for machine suspension.

### Default Implementations

- [Clock Implementations](suspendingclock/clock-implementations.md)

## See Also

### Clocks

- [Clock](clock.md) — A mechanism in which to measure time, and delay work until a given point in time.
- [ContinuousClock](continuousclock.md) — A clock that measures time that always increments and does not stop incrementing while the system is asleep.

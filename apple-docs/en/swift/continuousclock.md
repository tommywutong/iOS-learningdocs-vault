---
title: ContinuousClock
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/continuousclock
source_url: 'https://developer.apple.com/documentation/swift/continuousclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuousclock.json'
content_hash: 'sha256:cb0f3fd15c6be855'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ContinuousClock

<sub>Structure</sub>

A clock that measures time that always increments and does not stop incrementing while the system is asleep.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ContinuousClock
```

## Overview

`ContinuousClock` can be considered as a stopwatch style time. The frame of reference of the `Instant` may be bound to process launch, machine boot or some other locally defined reference point. This means that the instants are only comparable locally during the execution of a program.

This clock is suitable for high resolution measurements of execution.

## Relationships

- **Conforms To**: [Clock](clock.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Instant](continuousclock/instant.md) — A continuous point in time used for `ContinuousClock`.

### Initializers

- [init()](<continuousclock/init().md>)

### Instance Properties

- [systemEpoch](continuousclock/systemepoch.md)

### Type Properties

- [now](continuousclock/now-swift.type.property.md) — The current continuous instant.

### Default Implementations

- [Clock Implementations](continuousclock/clock-implementations.md)

## See Also

### Clocks

- [Clock](clock.md) — A mechanism in which to measure time, and delay work until a given point in time.
- [SuspendingClock](suspendingclock.md) — A clock that measures time that always increments but stops incrementing while the system is asleep.

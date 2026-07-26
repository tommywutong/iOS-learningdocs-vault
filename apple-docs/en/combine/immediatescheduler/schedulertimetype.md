---
title: ImmediateScheduler.SchedulerTimeType
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/immediatescheduler/schedulertimetype
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedulertimetype.json'
content_hash: 'sha256:8d881b00c2f96538'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ImmediateScheduler](../immediatescheduler.md)

# ImmediateScheduler.SchedulerTimeType

<sub>Structure</sub>

The time type used by the immediate scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerTimeType
```

## Relationships

- **Conforms To**: [Comparable](../../swift/comparable.md), [Equatable](../../swift/equatable.md), [Strideable](../../swift/strideable.md)

## Topics

### Declaring a scheduler timekeeping system

- [Stride](schedulertimetype/stride.md) — The increment by which the immediate scheduler counts time.

### Calculating time offsets

- [advanced(by:)](<schedulertimetype/advanced(by_).md>) — Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.
- [distance(to:)](<schedulertimetype/distance(to_).md>) — Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.

## See Also

### Declaring scheduler timekeeping and options

- [SchedulerOptions](scheduleroptions.md) — A type that defines options accepted by the immediate scheduler.

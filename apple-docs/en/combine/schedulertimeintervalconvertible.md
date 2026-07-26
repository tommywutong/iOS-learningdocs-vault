---
title: SchedulerTimeIntervalConvertible
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/schedulertimeintervalconvertible
source_url: 'https://developer.apple.com/documentation/combine/schedulertimeintervalconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/schedulertimeintervalconvertible.json'
content_hash: 'sha256:554e53d7079b4adb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# SchedulerTimeIntervalConvertible

<sub>Protocol</sub>

A protocol that provides a scheduler with an expression for relative time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SchedulerTimeIntervalConvertible
```

## Relationships

- **Conforming Types**: [Stride](immediatescheduler/schedulertimetype/stride.md)

## Topics

### Converting seconds to scheduler time intervals

- [microseconds(_:)](<schedulertimeintervalconvertible/microseconds(__).md>) — Converts the specified number of microseconds into an instance of this scheduler time type.
- [milliseconds(_:)](<schedulertimeintervalconvertible/milliseconds(__).md>) — Converts the specified number of milliseconds into an instance of this scheduler time type.
- [nanoseconds(_:)](<schedulertimeintervalconvertible/nanoseconds(__).md>) — Converts the specified number of nanoseconds into an instance of this scheduler time type.
- [seconds(_:)](<schedulertimeintervalconvertible/seconds(__)-2cv8t.md>) — Converts the specified number of seconds, as a floating-point value, into an instance of this scheduler time type.
- [seconds(_:)](<schedulertimeintervalconvertible/seconds(__)-3g8ay.md>) — Converts the specified number of seconds into an instance of this scheduler time type.

## See Also

### Schedulers

- [Scheduler](scheduler.md) — A protocol that defines when and how to execute a closure.
- [ImmediateScheduler](immediatescheduler.md) — A scheduler for performing synchronous actions.

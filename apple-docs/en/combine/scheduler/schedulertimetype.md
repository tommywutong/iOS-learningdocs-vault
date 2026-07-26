---
title: SchedulerTimeType
framework: Combine
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/scheduler/schedulertimetype
source_url: 'https://developer.apple.com/documentation/combine/scheduler/schedulertimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/scheduler/schedulertimetype.json'
content_hash: 'sha256:fc6b222fa2585336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Scheduler](../scheduler.md)

# SchedulerTimeType

<sub>Associated Type</sub>

Describes an instant in time for this scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SchedulerTimeType : Strideable where Self.SchedulerTimeType.Stride : SchedulerTimeIntervalConvertible
```

## See Also

### Declaring scheduler timekeeping and options

- [SchedulerOptions](scheduleroptions.md) — A type that defines options accepted by the scheduler.

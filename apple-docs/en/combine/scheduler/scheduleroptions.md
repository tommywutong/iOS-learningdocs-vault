---
title: SchedulerOptions
framework: Combine
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/scheduler/scheduleroptions
source_url: 'https://developer.apple.com/documentation/combine/scheduler/scheduleroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/scheduler/scheduleroptions.json'
content_hash: 'sha256:5b1bfce939748822'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Scheduler](../scheduler.md)

# SchedulerOptions

<sub>Associated Type</sub>

A type that defines options accepted by the scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SchedulerOptions
```

## Discussion

This type is freely definable by each `Scheduler`. Typically, operations that take a `Scheduler` parameter will also take `SchedulerOptions`.

## See Also

### Declaring scheduler timekeeping and options

- [SchedulerTimeType](schedulertimetype.md) — Describes an instant in time for this scheduler.

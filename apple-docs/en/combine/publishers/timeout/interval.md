---
title: interval
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/timeout/interval
source_url: 'https://developer.apple.com/documentation/combine/publishers/timeout/interval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timeout/interval.json'
content_hash: 'sha256:b41833087747e694'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Timeout](../timeout.md)

# interval

<sub>Instance Property</sub>

The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let interval: Context.SchedulerTimeType.Stride
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [scheduler](scheduler.md) — The scheduler on which to deliver events.
- [options](options.md) — Scheduler options that customize the delivery of elements.
- [customError](customerror.md) — A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.

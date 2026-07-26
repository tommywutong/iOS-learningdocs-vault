---
title: scheduler
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/throttle/scheduler
source_url: 'https://developer.apple.com/documentation/combine/publishers/throttle/scheduler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/throttle/scheduler.json'
content_hash: 'sha256:b4bd8cf5c0f625d9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Throttle](../throttle.md)

# scheduler

<sub>Instance Property</sub>

The scheduler on which to publish elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let scheduler: Context
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [interval](interval.md) — The interval in which to find and emit the most recent element.
- [latest](latest.md) — A Boolean value indicating whether to publish the most recent element.

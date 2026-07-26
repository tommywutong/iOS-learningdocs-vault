---
title: options
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/debounce/options
source_url: 'https://developer.apple.com/documentation/combine/publishers/debounce/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/debounce/options.json'
content_hash: 'sha256:85d574993a0c5d1e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Debounce](../debounce.md)

# options

<sub>Instance Property</sub>

Scheduler options that customize this publisher’s delivery of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let options: Context.SchedulerOptions?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [dueTime](duetime.md) — The amount of time the publisher should wait before publishing an element.
- [scheduler](scheduler.md) — The scheduler on which this publisher delivers elements.

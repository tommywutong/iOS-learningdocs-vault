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
doc_path: /documentation/combine/publishers/debounce/scheduler
source_url: 'https://developer.apple.com/documentation/combine/publishers/debounce/scheduler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/debounce/scheduler.json'
content_hash: 'sha256:11f1ad3d876b00ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Debounce](../debounce.md)

# scheduler

<sub>Instance Property</sub>

The scheduler on which this publisher delivers elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let scheduler: Context
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [dueTime](duetime.md) — The amount of time the publisher should wait before publishing an element.
- [options](options.md) — Scheduler options that customize this publisher’s delivery of elements.

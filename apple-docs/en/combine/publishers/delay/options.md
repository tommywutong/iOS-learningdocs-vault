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
doc_path: /documentation/combine/publishers/delay/options
source_url: 'https://developer.apple.com/documentation/combine/publishers/delay/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/delay/options.json'
content_hash: 'sha256:b5e4a3fe6bffaadd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Delay](../delay.md)

# options

<sub>Instance Property</sub>

Options relevant to the scheduler’s behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let options: Context.SchedulerOptions?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.
- [interval](interval.md) — The amount of time to delay.
- [tolerance](tolerance.md) — The allowed tolerance in firing delayed events.
- [scheduler](scheduler.md) — The scheduler to deliver the delayed events.

---
title: prefetch
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/buffer/prefetch
source_url: 'https://developer.apple.com/documentation/combine/publishers/buffer/prefetch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/buffer/prefetch.json'
content_hash: 'sha256:c7b669348747a265'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Buffer](../buffer.md)

# prefetch

<sub>Instance Property</sub>

The strategy for initially populating the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let prefetch: Publishers.PrefetchStrategy
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [size](size.md) — The maximum number of elements to store.
- [whenFull](whenfull.md) — The action to take when the buffer becomes full.

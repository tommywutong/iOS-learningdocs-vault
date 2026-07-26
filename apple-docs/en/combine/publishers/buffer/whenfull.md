---
title: whenFull
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/buffer/whenfull
source_url: 'https://developer.apple.com/documentation/combine/publishers/buffer/whenfull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/buffer/whenfull.json'
content_hash: 'sha256:ce49587e68b43c6d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Buffer](../buffer.md)

# whenFull

<sub>Instance Property</sub>

The action to take when the buffer becomes full.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let whenFull: Publishers.BufferingStrategy<Publishers.Buffer<Upstream>.Failure>
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [size](size.md) — The maximum number of elements to store.
- [prefetch](prefetch.md) — The strategy for initially populating the buffer.

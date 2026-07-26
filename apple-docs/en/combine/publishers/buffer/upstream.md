---
title: upstream
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/buffer/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/buffer/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/buffer/upstream.json'
content_hash: 'sha256:abe0ca864724e56b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Buffer](../buffer.md)

# upstream

<sub>Instance Property</sub>

The publisher from which this publisher receives elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [size](size.md) — The maximum number of elements to store.
- [prefetch](prefetch.md) — The strategy for initially populating the buffer.
- [whenFull](whenfull.md) — The action to take when the buffer becomes full.

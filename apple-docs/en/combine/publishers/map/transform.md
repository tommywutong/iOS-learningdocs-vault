---
title: transform
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/map/transform
source_url: 'https://developer.apple.com/documentation/combine/publishers/map/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/map/transform.json'
content_hash: 'sha256:d6520eea4a0c6f1f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Map](../map.md)

# transform

<sub>Instance Property</sub>

The closure that transforms elements from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let transform: (Upstream.Output) -> Output
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.

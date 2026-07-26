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
doc_path: /documentation/combine/publishers/throttle/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/throttle/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/throttle/upstream.json'
content_hash: 'sha256:961d7b04fe81a3f0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Throttle](../throttle.md)

# upstream

<sub>Instance Property</sub>

The publisher from which this publisher receives elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [interval](interval.md) — The interval in which to find and emit the most recent element.
- [scheduler](scheduler.md) — The scheduler on which to publish elements.
- [latest](latest.md) — A Boolean value indicating whether to publish the most recent element.

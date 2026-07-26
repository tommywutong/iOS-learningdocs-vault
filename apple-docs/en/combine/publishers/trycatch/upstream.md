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
doc_path: /documentation/combine/publishers/trycatch/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycatch/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycatch/upstream.json'
content_hash: 'sha256:9d25a026bfb42c10'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryCatch](../trycatch.md)

# upstream

<sub>Instance Property</sub>

The publisher from which this publisher receives its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [handler](handler.md) — A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher or throws an error.

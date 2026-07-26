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
doc_path: /documentation/combine/publishers/tryscan/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryscan/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryscan/upstream.json'
content_hash: 'sha256:ba29e1a034b344a2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryScan](../tryscan.md)

# upstream

<sub>Instance Property</sub>

The publisher that this publisher receives elements from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [initialResult](initialresult.md) — The previous result returned by the `nextPartialResult` closure.
- [nextPartialResult](nextpartialresult.md) — An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

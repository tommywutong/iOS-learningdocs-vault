---
title: nextPartialResult
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryscan/nextpartialresult
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryscan/nextpartialresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryscan/nextpartialresult.json'
content_hash: 'sha256:da2a3a3457ce8c5d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryScan](../tryscan.md)

# nextPartialResult

<sub>Instance Property</sub>

An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let nextPartialResult: (Output, Upstream.Output) throws -> Output
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher that this publisher receives elements from.
- [initialResult](initialresult.md) — The previous result returned by the `nextPartialResult` closure.

---
title: initialResult
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/scan/initialresult
source_url: 'https://developer.apple.com/documentation/combine/publishers/scan/initialresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/scan/initialresult.json'
content_hash: 'sha256:61d5b1433d70c95d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Scan](../scan.md)

# initialResult

<sub>Instance Property</sub>

The previous result returned by the `nextPartialResult` closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let initialResult: Output
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher that this publisher receives elements from.
- [nextPartialResult](nextpartialresult.md) — An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

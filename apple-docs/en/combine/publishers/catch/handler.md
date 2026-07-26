---
title: handler
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/catch/handler
source_url: 'https://developer.apple.com/documentation/combine/publishers/catch/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/catch/handler.json'
content_hash: 'sha256:2c338f708459417b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Catch](../catch.md)

# handler

<sub>Instance Property</sub>

A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let handler: (Upstream.Failure) -> NewPublisher
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.

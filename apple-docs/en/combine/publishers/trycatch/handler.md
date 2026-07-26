---
title: handler
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycatch/handler
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycatch/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycatch/handler.json'
content_hash: 'sha256:1851572c20355367'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryCatch](../trycatch.md)

# handler

<sub>Instance Property</sub>

A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher or throws an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let handler: (Upstream.Failure) throws -> NewPublisher
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives its elements.

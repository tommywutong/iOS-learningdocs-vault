---
title: 'init(upstream:handler:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/trycatch/init(upstream:handler:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycatch/init(upstream:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycatch/init%28upstream%3Ahandler%3A%29.json'
content_hash: 'sha256:ff60cc34a8c38be4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryCatch](../trycatch.md)

# init(upstream:handler:)

<sub>Initializer</sub>

Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or by throwing an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, handler: @escaping (Upstream.Failure) throws -> NewPublisher)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `handler` — A closure that accepts the upstream failure as input and either returns a publisher to replace the upstream publisher. If this closure throws an error, the publisher terminates with the thrown error.

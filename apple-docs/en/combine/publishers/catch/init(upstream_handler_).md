---
title: 'init(upstream:handler:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/catch/init(upstream:handler:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/catch/init(upstream:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/catch/init%28upstream%3Ahandler%3A%29.json'
content_hash: 'sha256:fbddb0690a41ccc1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Catch](../catch.md)

# init(upstream:handler:)

<sub>Initializer</sub>

Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, handler: @escaping (Upstream.Failure) -> NewPublisher)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `handler` — A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

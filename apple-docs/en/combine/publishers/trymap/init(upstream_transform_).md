---
title: 'init(upstream:transform:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/trymap/init(upstream:transform:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/trymap/init(upstream:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trymap/init%28upstream%3Atransform%3A%29.json'
content_hash: 'sha256:06c666714ebf9155'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryMap](../trymap.md)

# init(upstream:transform:)

<sub>Initializer</sub>

Creates a publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, transform: @escaping (Upstream.Output) throws -> Output)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `transform` — The error-throwing closure that transforms elements from the upstream publisher.

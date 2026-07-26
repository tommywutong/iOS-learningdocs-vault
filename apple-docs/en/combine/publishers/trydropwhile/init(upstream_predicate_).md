---
title: 'init(upstream:predicate:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/trydropwhile/init(upstream:predicate:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/trydropwhile/init(upstream:predicate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trydropwhile/init%28upstream%3Apredicate%3A%29.json'
content_hash: 'sha256:2ce3b300a901ba9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryDropWhile](../trydropwhile.md)

# init(upstream:predicate:)

<sub>Initializer</sub>

Creates a publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, predicate: @escaping (Publishers.TryDropWhile<Upstream>.Output) throws -> Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `predicate` — The error-throwing closure that indicates whether to drop the element.

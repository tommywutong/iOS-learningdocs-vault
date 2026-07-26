---
title: 'init(upstream:areInIncreasingOrder:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/comparison/init(upstream:areinincreasingorder:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/comparison/init(upstream:areinincreasingorder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/comparison/init%28upstream%3Aareinincreasingorder%3A%29.json'
content_hash: 'sha256:a49e2c7779e48384'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Comparison](../comparison.md)

# init(upstream:areInIncreasingOrder:)

<sub>Initializer</sub>

Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, areInIncreasingOrder: @escaping (Upstream.Output, Upstream.Output) -> Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives its elements.

- `areInIncreasingOrder` — A closure that receives two elements and returns true if they are in increasing order.

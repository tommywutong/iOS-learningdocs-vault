---
title: 'init(upstream:count:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/drop/init(upstream:count:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/drop/init(upstream:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/drop/init%28upstream%3Acount%3A%29.json'
content_hash: 'sha256:c9d72d999e067acc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Drop](../drop.md)

# init(upstream:count:)

<sub>Initializer</sub>

Creates a publisher that omits a specified number of elements before republishing later elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, count: Int)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `count` — The number of elements to drop.

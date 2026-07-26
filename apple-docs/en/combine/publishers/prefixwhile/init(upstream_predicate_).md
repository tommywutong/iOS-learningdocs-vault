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
doc_path: '/documentation/combine/publishers/prefixwhile/init(upstream:predicate:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefixwhile/init(upstream:predicate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefixwhile/init%28upstream%3Apredicate%3A%29.json'
content_hash: 'sha256:74826d9c65baef14'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [PrefixWhile](../prefixwhile.md)

# init(upstream:predicate:)

<sub>Initializer</sub>

Creates a publisher that republishes elements while a predicate closure indicates publishing should continue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, predicate: @escaping (Publishers.PrefixWhile<Upstream>.Output) -> Bool)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `predicate` — The closure that determines whether publishing should continue.

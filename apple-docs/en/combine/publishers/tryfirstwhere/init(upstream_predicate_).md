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
doc_path: '/documentation/combine/publishers/tryfirstwhere/init(upstream:predicate:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryfirstwhere/init(upstream:predicate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryfirstwhere/init%28upstream%3Apredicate%3A%29.json'
content_hash: 'sha256:6a716d33f0071130'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryFirstWhere](../tryfirstwhere.md)

# init(upstream:predicate:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, predicate: @escaping (Publishers.TryFirstWhere<Upstream>.Output) throws -> Bool)
```

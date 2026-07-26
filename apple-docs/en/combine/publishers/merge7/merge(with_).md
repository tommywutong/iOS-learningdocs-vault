---
title: 'merge(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/merge7/merge(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge7/merge(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge7/merge%28with%3A%29.json'
content_hash: 'sha256:b9318c7ab7914a1d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge7](../merge7.md)

# merge(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<P>(with other: P) -> Publishers.Merge8<A, B, C, D, E, F, G, P> where P : Publisher, G.Failure == P.Failure, G.Output == P.Output
```

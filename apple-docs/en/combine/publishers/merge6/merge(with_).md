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
doc_path: '/documentation/combine/publishers/merge6/merge(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge6/merge(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge6/merge%28with%3A%29.json'
content_hash: 'sha256:fdbaea275351d202'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge6](../merge6.md)

# merge(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<P>(with other: P) -> Publishers.Merge7<A, B, C, D, E, F, P> where P : Publisher, F.Failure == P.Failure, F.Output == P.Output
```

## See Also

### Merging elements

- [merge(with:_:)](<merge(with___).md>)

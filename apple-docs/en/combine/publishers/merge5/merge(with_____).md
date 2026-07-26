---
title: 'merge(with:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/merge5/merge(with:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge5/merge(with:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge5/merge%28with%3A_%3A_%3A%29.json'
content_hash: 'sha256:31abe5d6d9d91abb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge5](../merge5.md)

# merge(with:_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<Z, Y, X>(with z: Z, _ y: Y, _ x: X) -> Publishers.Merge8<A, B, C, D, E, Z, Y, X> where Z : Publisher, Y : Publisher, X : Publisher, E.Failure == Z.Failure, E.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output
```

## See Also

### Merging elements

- [merge(with:)](<merge(with_).md>)
- [merge(with:_:)](<merge(with___).md>)

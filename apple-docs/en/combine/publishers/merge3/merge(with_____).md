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
doc_path: '/documentation/combine/publishers/merge3/merge(with:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge3/merge(with:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge3/merge%28with%3A_%3A_%3A%29.json'
content_hash: 'sha256:6772da8d9038a682'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge3](../merge3.md)

# merge(with:_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<Z, Y, X>(with z: Z, _ y: Y, _ x: X) -> Publishers.Merge6<A, B, C, Z, Y, X> where Z : Publisher, Y : Publisher, X : Publisher, C.Failure == Z.Failure, C.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output
```

## See Also

### Merging elements

- [merge(with:)](<merge(with_).md>)
- [merge(with:_:)](<merge(with___).md>)
- [merge(with:_:_:_:)](<merge(with_______).md>)
- [merge(with:_:_:_:_:)](<merge(with_________).md>)

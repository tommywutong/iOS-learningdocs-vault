---
title: 'merge(with:_:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/merge/merge(with:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/merge/merge(with:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/merge/merge%28with%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0b74ddf61de16f22'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Merge](../merge.md)

# merge(with:_:_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<Z, Y, X, W>(with z: Z, _ y: Y, _ x: X, _ w: W) -> Publishers.Merge6<A, B, Z, Y, X, W> where Z : Publisher, Y : Publisher, X : Publisher, W : Publisher, B.Failure == Z.Failure, B.Output == Z.Output, Z.Failure == Y.Failure, Z.Output == Y.Output, Y.Failure == X.Failure, Y.Output == X.Output, X.Failure == W.Failure, X.Output == W.Output
```

## See Also

### Merging elements

- [merge(with:)](<merge(with_).md>)
- [merge(with:_:)](<merge(with___).md>)
- [merge(with:_:_:)](<merge(with_____).md>)
- [merge(with:_:_:_:_:)](<merge(with_________).md>)
- [merge(with:_:_:_:_:_:)](<merge(with___________).md>)

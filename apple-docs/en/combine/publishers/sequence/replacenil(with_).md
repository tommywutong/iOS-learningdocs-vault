---
title: 'replaceNil(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/replacenil(with:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/replacenil(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/replacenil%28with%3A%29.json'
content_hash: 'sha256:45919336d25e4ace'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# replaceNil(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceNil<T>(with output: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure> where Elements.Element == T?
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [scan(_:_:)](<scan(____).md>)
- [setFailureType(to:)](<setfailuretype(to_).md>)

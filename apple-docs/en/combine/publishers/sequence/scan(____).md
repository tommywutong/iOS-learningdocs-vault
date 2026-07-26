---
title: 'scan(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/scan(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/scan(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/scan%28_%3A_%3A%29.json'
content_hash: 'sha256:118f151c566b8c62'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# scan(_:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Publishers.Sequence<[T], Failure>
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [setFailureType(to:)](<setfailuretype(to_).md>)
- [replaceNil(with:)](<replacenil(with_).md>)

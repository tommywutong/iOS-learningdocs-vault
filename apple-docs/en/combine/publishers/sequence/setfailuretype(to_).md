---
title: 'setFailureType(to:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/setfailuretype(to:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/setfailuretype(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/setfailuretype%28to%3A%29.json'
content_hash: 'sha256:09a47e87f217a27c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# setFailureType(to:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setFailureType<E>(to error: E.Type) -> Publishers.Sequence<Elements, E> where E : Error
```

## See Also

### Mapping elements

- [map(_:)](<map(__).md>)
- [scan(_:_:)](<scan(____).md>)
- [replaceNil(with:)](<replacenil(with_).md>)

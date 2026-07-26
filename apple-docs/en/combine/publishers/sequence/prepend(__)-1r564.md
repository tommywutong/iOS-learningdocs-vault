---
title: 'prepend(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/prepend(_:)-1r564'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/prepend(_:)-1r564'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/prepend%28_%3A%29-1r564.json'
content_hash: 'sha256:2d52a1efa34bf1ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# prepend(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepend<S>(_ elements: S) -> Publishers.Sequence<Elements, Failure> where S : Sequence, Elements.Element == S.Element
```

## See Also

### Applying sequence operations to elements

- [dropFirst(_:)](<dropfirst(__).md>)
- [drop(while:)](<drop(while_).md>)
- [append(_:)](<append(__)-45rm8.md>)
- [append(_:)](<append(__)-3dj6k.md>)
- [append(_:)](<append(__)-2knh4.md>)
- [prepend(_:)](<prepend(__)-71f7p.md>)
- [prepend(_:)](<prepend(__)-2ros1.md>)
- [prefix(_:)](<prefix(__).md>)
- [prefix(while:)](<prefix(while_).md>)

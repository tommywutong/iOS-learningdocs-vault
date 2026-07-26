---
title: 'drop(while:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/sequence/drop(while:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence/drop%28while%3A%29.json'
content_hash: 'sha256:a72cc1bc710aa99e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Sequence](../sequence.md)

# drop(while:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop(while predicate: (Elements.Element) -> Bool) -> Publishers.Sequence<DropWhileSequence<Elements>, Failure>
```

## See Also

### Applying sequence operations to elements

- [dropFirst(_:)](<dropfirst(__).md>)
- [append(_:)](<append(__)-45rm8.md>)
- [append(_:)](<append(__)-3dj6k.md>)
- [append(_:)](<append(__)-2knh4.md>)
- [prepend(_:)](<prepend(__)-1r564.md>)
- [prepend(_:)](<prepend(__)-71f7p.md>)
- [prepend(_:)](<prepend(__)-2ros1.md>)
- [prefix(_:)](<prefix(__).md>)
- [prefix(while:)](<prefix(while_).md>)

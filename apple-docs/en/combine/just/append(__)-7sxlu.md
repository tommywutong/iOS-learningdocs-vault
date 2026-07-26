---
title: 'append(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/just/append(_:)-7sxlu'
source_url: 'https://developer.apple.com/documentation/combine/just/append(_:)-7sxlu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/append%28_%3A%29-7sxlu.json'
content_hash: 'sha256:061289aadf348f60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# append(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append<S>(_ elements: S) -> Publishers.Sequence<[Output], Just<Output>.Failure> where Output == S.Element, S : Sequence
```

## See Also

### Applying sequence operations to elements

- [dropFirst(_:)](<dropfirst(__).md>)
- [drop(while:)](<drop(while_).md>)
- [append(_:)](<append(__)-7eyqj.md>)
- [prepend(_:)](<prepend(__)-39e57.md>)
- [prepend(_:)](<prepend(__)-7fg73.md>)
- [prefix(_:)](<prefix(__).md>)
- [prefix(while:)](<prefix(while_).md>)

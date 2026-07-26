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
doc_path: '/documentation/combine/just/prepend(_:)-39e57'
source_url: 'https://developer.apple.com/documentation/combine/just/prepend(_:)-39e57'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/just/prepend%28_%3A%29-39e57.json'
content_hash: 'sha256:1efe007c3ffdbaa5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Just](../just.md)

# prepend(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prepend<S>(_ elements: S) -> Publishers.Sequence<[Output], Just<Output>.Failure> where Output == S.Element, S : Sequence
```

## See Also

### Applying sequence operations to elements

- [dropFirst(_:)](<dropfirst(__).md>)
- [drop(while:)](<drop(while_).md>)
- [append(_:)](<append(__)-7eyqj.md>)
- [append(_:)](<append(__)-7sxlu.md>)
- [prepend(_:)](<prepend(__)-7fg73.md>)
- [prefix(_:)](<prefix(__).md>)
- [prefix(while:)](<prefix(while_).md>)

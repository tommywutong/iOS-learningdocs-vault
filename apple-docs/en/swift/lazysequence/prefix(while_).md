---
title: 'prefix(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazysequence/prefix(while:)'
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/prefix(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/prefix%28while%3A%29.json'
content_hash: 'sha256:56d65f31a46bbc76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# prefix(while:)

<sub>Instance Method</sub>

Returns a lazy sequence of the initial consecutive elements that satisfy `predicate`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(while predicate: @escaping (Self.Elements.Element) -> Bool) -> LazyPrefixWhileSequence<Self.Elements>
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns `true` if the element should be included or `false` otherwise. Once `predicate` returns `false` it will not be called again.

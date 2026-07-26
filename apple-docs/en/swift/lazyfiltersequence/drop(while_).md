---
title: 'drop(while:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazyfiltersequence/drop(while:)'
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/drop(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/drop%28while%3A%29.json'
content_hash: 'sha256:7cab613fbadb2c2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# drop(while:)

<sub>Instance Method</sub>

Returns a lazy sequence that skips any initial elements that satisfy `predicate`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func drop(while predicate: @escaping (Self.Elements.Element) -> Bool) -> LazyDropWhileSequence<Self.Elements>
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns `true` if the element should be skipped or `false` otherwise. Once `predicate` returns `false` it will not be called again.

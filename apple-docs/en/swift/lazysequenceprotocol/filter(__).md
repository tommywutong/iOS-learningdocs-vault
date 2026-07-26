---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazysequenceprotocol/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/lazysequenceprotocol/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequenceprotocol/filter%28_%3A%29.json'
content_hash: 'sha256:3f3419a75e424411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequenceProtocol](../lazysequenceprotocol.md)

# filter(_:)

<sub>Instance Method</sub>

Returns the elements of `self` that satisfy `isIncluded`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filter(_ isIncluded: @escaping (Self.Elements.Element) -> Bool) -> LazyFilterSequence<Self.Elements>
```

## Discussion

> [!note] Note
> The elements of the result are computed on-demand, as the result is used. No buffering storage is allocated and each traversal step invokes `predicate` on one or more underlying elements.

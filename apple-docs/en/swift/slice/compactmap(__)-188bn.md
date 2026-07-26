---
title: 'compactMap(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/compactmap(_:)-188bn'
source_url: 'https://developer.apple.com/documentation/swift/slice/compactmap(_:)-188bn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/compactmap%28_%3A%29-188bn.json'
content_hash: 'sha256:04a63c2ccc3afce3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# compactMap(_:)

<sub>Instance Method</sub>

Returns the non-`nil` results of mapping the given transformation over this sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compactMap<ElementOfResult>(_ transform: @escaping (Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>
```

## Parameters

- `transform` — A closure that accepts an element of this sequence as its argument and returns an optional value.

## Discussion

Use this method to receive a sequence of non-optional values when your transformation produces an optional value.

> [!abstract] Complexity
> O(1)

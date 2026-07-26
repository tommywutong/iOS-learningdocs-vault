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
doc_path: '/documentation/swift/collectiondifference/prefix(while:)'
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/prefix(while:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/prefix%28while%3A%29.json'
content_hash: 'sha256:d7b97d8ac5df9c3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# prefix(while:)

<sub>Instance Method</sub>

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

## Parameters

- `predicate` — A closure that takes an element of the sequence as its argument and returns `true` if the element should be included or `false` if it should be excluded. Once the predicate returns `false` it will not be called again.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

---
title: inferringMoves()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectiondifference/inferringmoves()
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/inferringmoves()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/inferringmoves%28%29.json'
content_hash: 'sha256:906beb0ec4c0b41c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# inferringMoves()

<sub>Instance Method</sub>

Returns a new collection difference with associations between individual elements that have been removed and inserted only once.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func inferringMoves() -> CollectionDifference<ChangeElement>
```

## Return Value

A collection difference with all possible moves inferred.

## Discussion

> [!abstract] Complexity
> O(_n_) where _n_ is the number of collection differences.

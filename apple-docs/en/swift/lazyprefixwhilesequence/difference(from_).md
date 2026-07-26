---
title: 'difference(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/lazyprefixwhilesequence/difference(from:)'
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/difference(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilesequence/difference%28from%3A%29.json'
content_hash: 'sha256:90020064777d8eed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyPrefixWhileSequence](../lazyprefixwhilesequence.md)

# difference(from:)

<sub>Instance Method</sub>

Returns the difference needed to produce this collection’s ordered elements from the given collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func difference<C>(from other: C) -> CollectionDifference<Self.Element> where C : BidirectionalCollection, Self.Element == C.Element
```

## Parameters

- `other` — The base state.

## Return Value

The difference needed to produce this collection’s ordered elements from the given collection.

## Discussion

This function does not infer element moves. If you need to infer moves, call the `inferringMoves()` method on the resulting difference.

> [!abstract] Complexity
> Worst case performance is O(_n_ * _m_), where _n_ is the count of this collection and _m_ is `other.count`. You can expect faster execution when the collections share many common elements, or if `Element` conforms to `Hashable`.

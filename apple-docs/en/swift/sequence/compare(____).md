---
title: 'compare(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/compare(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/compare(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/compare%28_%3A_%3A%29.json'
content_hash: 'sha256:ac5e0ce15aeb2e02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# compare(_:_:)

<sub>Instance Method</sub>

If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare<Comparator>(_ lhs: Comparator.Compared, _ rhs: Comparator.Compared) -> ComparisonResult where Comparator : SortComparator, Comparator == Self.Element
```

## Discussion

The first element of the sequence of comparators specifies the primary comparator to be used in sorting the sequence’s elements. Any subsequent comparators are used to further refine the order of elements with equal values.

---
title: 'sort(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/sort(using:)-9a05g'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/sort(using:)-9a05g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/sort%28using%3A%29-9a05g.json'
content_hash: 'sha256:0102134d7a06ac0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# sort(using:)

<sub>Instance Method</sub>

Sorts the collection using the given array of `SortComparator`s to compare elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func sort<S, Comparator>(using comparators: S) where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```

## Parameters

- `comparators` — An array of comparators used to compare elements. The first comparator specifies the primary comparator to be used in sorting the sequence’s elements. Any subsequent comparators are used to further refine the order of elements with equal values.

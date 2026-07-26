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
doc_path: '/documentation/swift/mutablecollection/sort(using:)-694fo'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/sort(using:)-694fo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/sort%28using%3A%29-694fo.json'
content_hash: 'sha256:05e31d46e94428db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# sort(using:)

<sub>Instance Method</sub>

Sorts the collection using the given comparator to compare elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func sort<Comparator>(using comparator: Comparator) where Comparator : SortComparator, Self.Element == Comparator.Compared
```

## Parameters

- `comparator` — The sort comparator used to compare elements.

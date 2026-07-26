---
title: 'remove(_:within:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/remove(_:within:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/remove(_:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/remove%28_%3Awithin%3A%29.json'
content_hash: 'sha256:57697044e3448a3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# remove(_:within:)

<sub>Instance Method</sub>

Removes the range that contains only the specified index from the range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func remove<C>(_ index: Bound, within collection: C) where Bound == C.Index, C : Collection
```

## Parameters

- `index` — The index to remove from the range set. `index` must be a valid index of `collection` that isn’t the collection’s `endIndex`.

- `collection` — The collection that contains `index`.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the number of ranges in the range set.

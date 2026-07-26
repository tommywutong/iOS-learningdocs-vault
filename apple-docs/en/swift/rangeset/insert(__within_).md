---
title: 'insert(_:within:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/insert(_:within:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/insert(_:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/insert%28_%3Awithin%3A%29.json'
content_hash: 'sha256:79c4780b53a47fc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# insert(_:within:)

<sub>Instance Method</sub>

Inserts a range that contains only the specified index into the range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert<C>(_ index: Bound, within collection: C) -> Bool where Bound == C.Index, C : Collection
```

## Parameters

- `index` — The index to insert into the range set. `index` must be a valid index of `collection` that isn’t the collection’s `endIndex`.

- `collection` — The collection that contains `index`.

## Return Value

`true` if the range set was modified, or `false` if the given `index` was already in the range set.

## Discussion

> [!abstract] Complexity
> O(_n_), where _n_ is the number of ranges in the range set.

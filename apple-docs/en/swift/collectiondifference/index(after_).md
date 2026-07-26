---
title: 'index(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectiondifference/index(after:)'
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/index(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/index%28after%3A%29.json'
content_hash: 'sha256:444aed9f7a6e1e57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# index(after:)

<sub>Instance Method</sub>

Returns the position immediately after the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(after index: CollectionDifference<ChangeElement>.Index) -> CollectionDifference<ChangeElement>.Index
```

## Return Value

The index value immediately after `i`.

## Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

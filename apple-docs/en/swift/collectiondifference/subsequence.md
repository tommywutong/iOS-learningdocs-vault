---
title: CollectionDifference.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectiondifference/subsequence
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/subsequence.json'
content_hash: 'sha256:b64fc11f5458834e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# CollectionDifference.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<CollectionDifference<ChangeElement>>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

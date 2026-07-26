---
title: RangeSet.Ranges.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rangeset/ranges-swift.struct/subsequence
source_url: 'https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/ranges-swift.struct/subsequence.json'
content_hash: 'sha256:a1ec8f8f49b9769d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [RangeSet](../../rangeset.md) · [Ranges](../ranges-swift.struct.md)

# RangeSet.Ranges.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<RangeSet<Bound>.Ranges>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

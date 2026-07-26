---
title: UInt64.Words.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint64/words-swift.struct/subsequence
source_url: 'https://developer.apple.com/documentation/swift/uint64/words-swift.struct/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/words-swift.struct/subsequence.json'
content_hash: 'sha256:f827b3bb82d87870'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt64](../../uint64.md) · [Words](../words-swift.struct.md)

# UInt64.Words.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<UInt64.Words>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

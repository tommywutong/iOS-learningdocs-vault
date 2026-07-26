---
title: ClosedRange.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/closedrange/subsequence
source_url: 'https://developer.apple.com/documentation/swift/closedrange/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/subsequence.json'
content_hash: 'sha256:b37c136f5a82af2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# ClosedRange.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<ClosedRange<Bound>>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

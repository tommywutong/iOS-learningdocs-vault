---
title: SubSequence
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collection/subsequence
source_url: 'https://developer.apple.com/documentation/swift/collection/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/subsequence.json'
content_hash: 'sha256:69c49aeafe4cc08b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# SubSequence

<sub>Associated Type</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SubSequence : Collection = Slice<Self> where Self.Element == Self.SubSequence.Element, Self.SubSequence == Self.SubSequence.SubSequence
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

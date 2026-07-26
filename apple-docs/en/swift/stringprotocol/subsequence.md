---
title: SubSequence
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stringprotocol/subsequence
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/subsequence.json'
content_hash: 'sha256:73e867454b2f2825'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# SubSequence

<sub>Associated Type</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype SubSequence = Substring
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

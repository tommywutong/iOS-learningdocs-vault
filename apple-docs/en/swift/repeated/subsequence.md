---
title: Repeated.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/repeated/subsequence
source_url: 'https://developer.apple.com/documentation/swift/repeated/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/repeated/subsequence.json'
content_hash: 'sha256:5cfe3110d0203631'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Repeated](../repeated.md)

# Repeated.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<Repeated<Element>>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

---
title: EnumeratedSequence.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/enumeratedsequence/subsequence
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/subsequence.json'
content_hash: 'sha256:b17ad3882045ae8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# EnumeratedSequence.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<EnumeratedSequence<Base>>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

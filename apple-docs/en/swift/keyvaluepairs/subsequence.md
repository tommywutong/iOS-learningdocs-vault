---
title: KeyValuePairs.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyvaluepairs/subsequence
source_url: 'https://developer.apple.com/documentation/swift/keyvaluepairs/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyvaluepairs/subsequence.json'
content_hash: 'sha256:549ac9b9f6a4bf77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyValuePairs](../keyvaluepairs.md)

# KeyValuePairs.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<KeyValuePairs<Key, Value>>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

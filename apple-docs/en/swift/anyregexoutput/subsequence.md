---
title: AnyRegexOutput.SubSequence
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyregexoutput/subsequence
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/subsequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/subsequence.json'
content_hash: 'sha256:e7f39f72fc1a4919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRegexOutput](../anyregexoutput.md)

# AnyRegexOutput.SubSequence

<sub>Type Alias</sub>

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias SubSequence = Slice<AnyRegexOutput>
```

## Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

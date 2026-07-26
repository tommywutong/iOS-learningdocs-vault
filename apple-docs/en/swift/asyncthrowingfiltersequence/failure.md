---
title: AsyncThrowingFilterSequence.Failure
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingfiltersequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingfiltersequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingfiltersequence/failure.json'
content_hash: 'sha256:cf6354fb18d79cdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingFilterSequence](../asyncthrowingfiltersequence.md)

# AsyncThrowingFilterSequence.Failure

<sub>Type Alias</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = any Error
```

## Discussion

The filter sequence produces errors from either the base sequence or the filtering closure.

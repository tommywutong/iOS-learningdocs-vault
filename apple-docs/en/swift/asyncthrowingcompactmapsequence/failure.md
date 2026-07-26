---
title: AsyncThrowingCompactMapSequence.Failure
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingcompactmapsequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingcompactmapsequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingcompactmapsequence/failure.json'
content_hash: 'sha256:1778b15d5b75897b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingCompactMapSequence](../asyncthrowingcompactmapsequence.md)

# AsyncThrowingCompactMapSequence.Failure

<sub>Type Alias</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = any Error
```

## Discussion

The compact map sequence produces errors from either the base sequence or the transforming closure.

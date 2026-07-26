---
title: AsyncThrowingDropWhileSequence.Failure
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingdropwhilesequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingdropwhilesequence/failure.json'
content_hash: 'sha256:6c6034f1b93b5e73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingDropWhileSequence](../asyncthrowingdropwhilesequence.md)

# AsyncThrowingDropWhileSequence.Failure

<sub>Type Alias</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = any Error
```

## Discussion

The drop-while sequence produces errors from either the base sequence or the filtering closure.

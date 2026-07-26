---
title: AsyncThrowingPrefixWhileSequence.Failure
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingprefixwhilesequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingprefixwhilesequence/failure.json'
content_hash: 'sha256:baedb0b039ffb741'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingPrefixWhileSequence](../asyncthrowingprefixwhilesequence.md)

# AsyncThrowingPrefixWhileSequence.Failure

<sub>Type Alias</sub>

The type of error produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = any Error
```

## Discussion

The prefix-while sequence produces errors from either the base sequence or the filtering closure.

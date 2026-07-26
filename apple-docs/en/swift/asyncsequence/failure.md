---
title: Failure
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncsequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/failure.json'
content_hash: 'sha256:eccaa78d27073000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# Failure

<sub>Associated Type</sub>

The type of errors produced when iteration over the sequence fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Failure = any Error where Self.Failure == Self.AsyncIterator.Failure
```

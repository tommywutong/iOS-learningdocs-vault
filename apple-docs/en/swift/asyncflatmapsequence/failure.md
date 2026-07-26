---
title: AsyncFlatMapSequence.Failure
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncflatmapsequence/failure
source_url: 'https://developer.apple.com/documentation/swift/asyncflatmapsequence/failure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncflatmapsequence/failure.json'
content_hash: 'sha256:9208de07223f7e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncFlatMapSequence](../asyncflatmapsequence.md)

# AsyncFlatMapSequence.Failure

<sub>Type Alias</sub>

The type of error produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Failure = Base.Failure
```

## Discussion

The flat map sequence produces the type of error in the base asynchronous sequence. By construction, the sequence produced by the `transform` closure must either produce this type of error or not produce errors at all.

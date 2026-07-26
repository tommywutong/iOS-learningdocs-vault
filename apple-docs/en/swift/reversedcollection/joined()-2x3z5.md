---
title: joined()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/reversedcollection/joined()-2x3z5
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/joined()-2x3z5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/joined%28%29-2x3z5.json'
content_hash: 'sha256:bce29de9017d62e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ReversedCollection](../reversedcollection.md)

# joined()

<sub>Instance Method</sub>

Returns a lazy sequence that concatenates the elements of this sequence of sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> LazySequence<FlattenSequence<Self.Elements>>
```

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
doc_path: /documentation/swift/lazysequence/joined()-2zoe4
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/joined()-2zoe4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/joined%28%29-2zoe4.json'
content_hash: 'sha256:d2fe28b08be99327'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# joined()

<sub>Instance Method</sub>

Returns a lazy sequence that concatenates the elements of this sequence of sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> LazySequence<FlattenSequence<Self.Elements>>
```

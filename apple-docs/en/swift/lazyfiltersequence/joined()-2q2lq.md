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
doc_path: /documentation/swift/lazyfiltersequence/joined()-2q2lq
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/joined()-2q2lq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/joined%28%29-2q2lq.json'
content_hash: 'sha256:06c27796516c2d14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# joined()

<sub>Instance Method</sub>

Returns a lazy sequence that concatenates the elements of this sequence of sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> LazySequence<FlattenSequence<Self.Elements>>
```

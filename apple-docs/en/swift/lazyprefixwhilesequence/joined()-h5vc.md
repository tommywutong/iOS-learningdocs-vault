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
doc_path: /documentation/swift/lazyprefixwhilesequence/joined()-h5vc
source_url: 'https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/joined()-h5vc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyprefixwhilesequence/joined%28%29-h5vc.json'
content_hash: 'sha256:fbfdc32077383e29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyPrefixWhileSequence](../lazyprefixwhilesequence.md)

# joined()

<sub>Instance Method</sub>

Returns a lazy sequence that concatenates the elements of this sequence of sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> LazySequence<FlattenSequence<Self.Elements>>
```

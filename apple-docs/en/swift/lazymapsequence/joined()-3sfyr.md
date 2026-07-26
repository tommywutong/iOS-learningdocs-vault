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
doc_path: /documentation/swift/lazymapsequence/joined()-3sfyr
source_url: 'https://developer.apple.com/documentation/swift/lazymapsequence/joined()-3sfyr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazymapsequence/joined%28%29-3sfyr.json'
content_hash: 'sha256:49a1e143debba1d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyMapSequence](../lazymapsequence.md)

# joined()

<sub>Instance Method</sub>

Returns a lazy sequence that concatenates the elements of this sequence of sequences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined() -> LazySequence<FlattenSequence<Self.Elements>>
```

---
title: lazy
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dropwhilesequence/lazy
source_url: 'https://developer.apple.com/documentation/swift/dropwhilesequence/lazy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dropwhilesequence/lazy.json'
content_hash: 'sha256:1fece1455b3cb0c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DropWhileSequence](../dropwhilesequence.md)

# lazy

<sub>Instance Property</sub>

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lazy: LazySequence<Self> { get }
```

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
doc_path: /documentation/swift/discontiguousslice/lazy
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/lazy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/lazy.json'
content_hash: 'sha256:27c721dd52324830'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# lazy

<sub>Instance Property</sub>

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lazy: LazySequence<Self> { get }
```

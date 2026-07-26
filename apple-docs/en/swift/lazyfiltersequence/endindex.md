---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyfiltersequence/endindex
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/endindex.json'
content_hash: 'sha256:a7d1140d42449c30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: LazyFilterSequence<Base>.Index { get }
```

## Discussion

`endIndex` is always reachable from `startIndex` by zero or more applications of `index(after:)`.

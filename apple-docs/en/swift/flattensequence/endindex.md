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
doc_path: /documentation/swift/flattensequence/endindex
source_url: 'https://developer.apple.com/documentation/swift/flattensequence/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/flattensequence/endindex.json'
content_hash: 'sha256:403cf387412a6480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FlattenSequence](../flattensequence.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: FlattenSequence<Base>.Index { get }
```

## Discussion

`endIndex` is not a valid argument to `subscript`, and is always reachable from `startIndex` by zero or more applications of `index(after:)`.

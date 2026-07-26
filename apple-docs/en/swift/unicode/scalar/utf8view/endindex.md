---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/utf8view/endindex
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/utf8view/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/utf8view/endindex.json'
content_hash: 'sha256:09dbb6c901cd2284'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [UTF8View](../utf8view.md)

# endIndex

<sub>Instance Property</sub>

The “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Int { get }
```

## Discussion

If the collection is empty, `endIndex` is equal to `startIndex`.

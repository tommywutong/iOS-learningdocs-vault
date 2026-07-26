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
doc_path: /documentation/swift/anycollection/endindex
source_url: 'https://developer.apple.com/documentation/swift/anycollection/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anycollection/endindex.json'
content_hash: 'sha256:4414d49b86314ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyCollection](../anycollection.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: AnyCollection<Element>.Index { get }
```

## Discussion

`endIndex` is always reachable from `startIndex` by zero or more applications of `index(after:)`.

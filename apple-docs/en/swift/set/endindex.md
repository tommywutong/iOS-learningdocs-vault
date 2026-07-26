---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/endindex
source_url: 'https://developer.apple.com/documentation/swift/set/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/endindex.json'
content_hash: 'sha256:bbb2a641aa489572'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# endIndex

<sub>Instance Property</sub>

The “past the end” position for the set—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: Set<Element>.Index { get }
```

## Discussion

If the set is empty, `endIndex` is equal to `startIndex`.

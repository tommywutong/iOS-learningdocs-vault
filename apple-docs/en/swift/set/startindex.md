---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/startindex
source_url: 'https://developer.apple.com/documentation/swift/set/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/startindex.json'
content_hash: 'sha256:13868798a2847663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# startIndex

<sub>Instance Property</sub>

The starting position for iterating members of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: Set<Element>.Index { get }
```

## Discussion

If the set is empty, `startIndex` is equal to `endIndex`.

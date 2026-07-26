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
doc_path: /documentation/swift/contiguousarray/startindex
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/startindex.json'
content_hash: 'sha256:884962aaa97ab6b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: Int { get }
```

## Discussion

For an instance of `ContiguousArray`, `startIndex` is always zero. If the array is empty, `startIndex` is equal to `endIndex`.

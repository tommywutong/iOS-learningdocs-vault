---
title: startIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rangeset/ranges-swift.struct/startindex
source_url: 'https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/ranges-swift.struct/startindex.json'
content_hash: 'sha256:2ae491e3bd3901c0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [RangeSet](../../rangeset.md) · [Ranges](../ranges-swift.struct.md)

# startIndex

<sub>Instance Property</sub>

The position of the first element in a nonempty collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: RangeSet<Bound>.Ranges.Index { get }
```

## Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

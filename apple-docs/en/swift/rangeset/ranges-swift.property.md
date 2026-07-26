---
title: ranges
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rangeset/ranges-swift.property
source_url: 'https://developer.apple.com/documentation/swift/rangeset/ranges-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/ranges-swift.property.json'
content_hash: 'sha256:657db2e4d51137dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# ranges

<sub>Instance Property</sub>

A collection of the ranges that make up the range set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ranges: RangeSet<Bound>.Ranges { get }
```

## Discussion

The ranges that you access by using `ranges` never overlap, are never empty, and are always in increasing order.

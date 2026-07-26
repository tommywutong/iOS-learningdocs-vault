---
title: count
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/discontiguousslice/count
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/count.json'
content_hash: 'sha256:6fc0a21ce67ac066'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# count

<sub>Instance Property</sub>

The number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O(_n_) operation.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.

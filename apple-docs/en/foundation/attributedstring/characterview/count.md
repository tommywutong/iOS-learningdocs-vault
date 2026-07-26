---
title: count
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/characterview/count
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/characterview/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/characterview/count.json'
content_hash: 'sha256:90c9f86a29ecd906'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [CharacterView](../characterview.md)

# count

<sub>Instance Property</sub>

The number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O(_n_) operation.

Complexity: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.

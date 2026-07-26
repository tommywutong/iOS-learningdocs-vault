---
title: 'compare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/compare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/compare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/compare%28_%3A%29.json'
content_hash: 'sha256:63455ab89ac4edad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# compare(_:)

<sub>Instance Method</sub>

Indicates the depth-first traversal order of the receiving index path and another index path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ otherObject: IndexPath) -> ComparisonResult
```

## Parameters

- `otherObject` — Index path to compare. This value must not be `nil`. If the value is `nil`, the behavior is undefined.

## Return Value

The depth-first traversal ordering of the receiving index path and `indexPath`.

## Discussion

- [NSOrderedAscending](../comparisonresult/orderedascending.md): The receiving index path comes before `indexPath`.
- [NSOrderedDescending](../comparisonresult/ordereddescending.md): The receiving index path comes after `indexPath`.
- [NSOrderedSame](../comparisonresult/orderedsame.md): The receiving index path and `indexPath` are the same index path.

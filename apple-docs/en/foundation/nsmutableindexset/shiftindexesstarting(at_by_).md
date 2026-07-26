---
title: 'shiftIndexesStarting(at:by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableindexset/shiftindexesstarting(at:by:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableindexset/shiftindexesstarting(at:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableindexset/shiftindexesstarting%28at%3Aby%3A%29.json'
content_hash: 'sha256:6b27e5405d627c81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableIndexSet](../nsmutableindexset.md)

# shiftIndexesStarting(at:by:)

<sub>Instance Method</sub>

Shifts a group of indexes to the left or the right within the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func shiftIndexesStarting(at index: Int, by delta: Int)
```

## Parameters

- `index` — Head of the group of indexes to shift.

- `delta` — Amount and direction of the shift. Positive integers shift the indexes to the right. Negative integers shift the indexes to the left.

## Discussion

The group of indexes shifted is made up by `index` and the indexes that follow it in the set.

A left shift deletes the indexes in a range the length of `delta` preceding `index` from the set.

A right shift inserts empty space in the range `(``index``,``delta``)` in the receiver.

The resulting indexes must all be in the range `0 .. NSNotFound - 1`.

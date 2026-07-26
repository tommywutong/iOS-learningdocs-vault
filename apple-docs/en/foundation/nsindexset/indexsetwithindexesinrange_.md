---
title: 'indexSetWithIndexesInRange:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/indexsetwithindexesinrange:'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/indexsetwithindexesinrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/indexsetwithindexesinrange%3A.json'
content_hash: 'sha256:45ef66e7fe4cac7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# indexSetWithIndexesInRange:

<sub>Type Method</sub>

Creates an index set with an index range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) indexSetWithIndexesInRange:(NSRange) range;
```

## Parameters

- `range` — An index range. Must be in the range `0 .. NSNotFound - 1`.

## Return Value

[NSIndexSet](../nsindexset.md) object containing `indexRange`.

## Discussion

The resulting index set has a [firstIndex](firstindex.md) equal to the `location` of `indexRange`, and a [count](count.md) equal to the `length` of `indexRange`. Specifying a zero-length range results in an empty index set.

## See Also

### Creating Index Sets

- [indexSet](indexset.md) — Creates an empty index set.
- [indexSetWithIndex:](indexsetwithindex_.md) — Creates an index set with an index.
- [- initWithIndex:](<init(index_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index.
- [- initWithIndexesInRange:](<init(indexesin_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index range.
- [- initWithIndexSet:](<init(indexset_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index set.

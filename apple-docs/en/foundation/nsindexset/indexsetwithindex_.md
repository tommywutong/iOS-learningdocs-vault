---
title: 'indexSetWithIndex:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/indexsetwithindex:'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/indexsetwithindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/indexsetwithindex%3A.json'
content_hash: 'sha256:2d29a12169b56611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# indexSetWithIndex:

<sub>Type Method</sub>

Creates an index set with an index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) indexSetWithIndex:(NSUInteger) value;
```

## Parameters

- `value` — An index. Must be in the range `0 .. NSNotFound - 1`.

## Return Value

[NSIndexSet](../nsindexset.md) object containing `index`.

## See Also

### Creating Index Sets

- [indexSet](indexset.md) — Creates an empty index set.
- [indexSetWithIndexesInRange:](indexsetwithindexesinrange_.md) — Creates an index set with an index range.
- [- initWithIndex:](<init(index_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index.
- [- initWithIndexesInRange:](<init(indexesin_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index range.
- [- initWithIndexSet:](<init(indexset_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index set.

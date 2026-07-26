---
title: 'init(index:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/init(index:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/init(index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/init%28index%3A%29.json'
content_hash: 'sha256:174ac9c30615aa1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# init(index:)

<sub>Initializer</sub>

Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(index value: Int)
```

## Parameters

- `value` — An index. Must be in the range `0 .. NSNotFound - 1`.

## Return Value

Initialized [NSIndexSet](../nsindexset.md) object with `index`.

## See Also

### Creating Index Sets

- [- initWithIndexesInRange:](<init(indexesin_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index range.
- [- initWithIndexSet:](<init(indexset_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index set.

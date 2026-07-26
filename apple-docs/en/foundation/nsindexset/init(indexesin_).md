---
title: 'init(indexesIn:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/init(indexesin:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/init(indexesin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/init%28indexesin%3A%29.json'
content_hash: 'sha256:c83c231a4dc07999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# init(indexesIn:)

<sub>Initializer</sub>

Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(indexesIn range: NSRange)
```

## Parameters

- `range` — An index range. Must be in the range `0 .. NSNotFound - 1`..

## Return Value

Initialized [NSIndexSet](../nsindexset.md) object with `indexRange`.

## Discussion

This method raises an [NSRangeException](../nsexceptionname/rangeexception.md) when `indexRange` would add an index that exceeds the maximum allowed value for unsigned integers.

The resulting index set has a [firstIndex](firstindex.md) equal to the `location` of `indexRange`, and a [count](count.md) equal to the `length` of `indexRange`. Specifying a zero-length range results in an empty index set.

This method is a designated initializer for [NSIndexSet](../nsindexset.md).

## See Also

### Creating Index Sets

- [- initWithIndex:](<init(index_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index.
- [- initWithIndexSet:](<init(indexset_).md>) — Initializes an allocated [NSIndexSet](../nsindexset.md) object with an index set.

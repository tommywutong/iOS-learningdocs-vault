---
title: 'indexPathWithIndexes:length:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/indexpathwithindexes:length:'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/indexpathwithindexes:length:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/indexpathwithindexes%3Alength%3A.json'
content_hash: 'sha256:5f10acd9b5718acc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# indexPathWithIndexes:length:

<sub>Type Method</sub>

Creates an index path with one or more nodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) indexPathWithIndexes:(const NSUInteger[]) indexes length:(NSUInteger) length;
```

## Parameters

- `indexes` — Array of indexes to make up the index path.

- `length` — Number of nodes to include in the index path.

## Return Value

Index path with `indexes` up to `length`.

## See Also

### Creating and Initializing Index Paths

- [indexPathWithIndex:](indexpathwithindex_.md) — Creates a one-node index path.
- [- initWithIndex:](<init(index_).md>) — Initializes an index path with a single node.
- [- initWithIndexes:length:](<init(indexes_length_).md>) — Initializes an index path with the given nodes and length.

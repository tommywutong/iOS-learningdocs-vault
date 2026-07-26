---
title: 'indexPathWithIndex:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/indexpathwithindex:'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/indexpathwithindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/indexpathwithindex%3A.json'
content_hash: 'sha256:f0157471f1c561b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# indexPathWithIndex:

<sub>Type Method</sub>

Creates a one-node index path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) indexPathWithIndex:(NSUInteger) index;
```

## Parameters

- `index` — Index of the item in node 0 to point to.

## Return Value

One-node index path with `index`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Creating and Initializing Index Paths

- [indexPathWithIndexes:length:](indexpathwithindexes_length_.md) — Creates an index path with one or more nodes.
- [- initWithIndex:](<init(index_).md>) — Initializes an index path with a single node.
- [- initWithIndexes:length:](<init(indexes_length_).md>) — Initializes an index path with the given nodes and length.

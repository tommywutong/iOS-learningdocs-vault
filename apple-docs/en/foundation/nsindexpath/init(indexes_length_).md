---
title: 'init(indexes:length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/init(indexes:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/init(indexes:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/init%28indexes%3Alength%3A%29.json'
content_hash: 'sha256:170cd24db2728b5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# init(indexes:length:)

<sub>Initializer</sub>

Initializes an index path with the given nodes and length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(indexes: UnsafePointer<Int>?, length: Int)
```

## Parameters

- `indexes` — Array of indexes to make up the index path.

- `length` — Number of nodes to include in the index path.

## Return Value

Initialized [NSIndexPath](../nsindexpath.md) object with `indexes` up to `length`.

## Discussion

This method is a designated initializer of [NSIndexPath](../nsindexpath.md).

## See Also

### Creating and Initializing Index Paths

- [- initWithIndex:](<init(index_).md>) — Initializes an index path with a single node.

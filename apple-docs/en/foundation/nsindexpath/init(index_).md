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
doc_path: '/documentation/foundation/nsindexpath/init(index:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/init(index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/init%28index%3A%29.json'
content_hash: 'sha256:c6096ac3e2e86934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# init(index:)

<sub>Initializer</sub>

Initializes an index path with a single node.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(index: Int)
```

## Parameters

- `index` — Index of the item in node 0 to point to.

## Return Value

Initialized [NSIndexPath](../nsindexpath.md) object representing a one-node index path with `index`.

## See Also

### Creating and Initializing Index Paths

- [- initWithIndexes:length:](<init(indexes_length_).md>) — Initializes an index path with the given nodes and length.

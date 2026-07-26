---
title: 'adding(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/adding(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/adding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/adding%28_%3A%29.json'
content_hash: 'sha256:338ebeeee2a34591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# adding(_:)

<sub>Instance Method</sub>

Returns an index path containing the nodes in the receiving index path plus another given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func adding(_ index: Int) -> IndexPath
```

## Parameters

- `index` — Index to append to the index path’s indexes.

## Return Value

A new index path containing the receiving index path’s indexes and `index`.

## See Also

### Adding and Removing Nodes

- [- indexPathByRemovingLastIndex](<removinglastindex().md>) — Returns an index path with the nodes in the receiving index path, excluding the last one.

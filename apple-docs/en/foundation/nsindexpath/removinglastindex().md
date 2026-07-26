---
title: removingLastIndex()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexpath/removinglastindex()
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/removinglastindex()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/removinglastindex%28%29.json'
content_hash: 'sha256:56b1de4e67e0a8a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# removingLastIndex()

<sub>Instance Method</sub>

Returns an index path with the nodes in the receiving index path, excluding the last one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removingLastIndex() -> IndexPath
```

## Return Value

A new index path with the receiving index path’s indexes, excluding the last one.

## Discussion

Returns an empty `NSIndexPath` instance if the receiving index path’s length is 1 or less.

### Special Considerations

In OS X v10.4 this method returns `nil` when the length of the receiving index path is 1 or less. On iOS and macOS 10.5 and later this method never returns `nil`.

## See Also

### Adding and Removing Nodes

- [- indexPathByAddingIndex:](<adding(__).md>) — Returns an index path containing the nodes in the receiving index path plus another given index.

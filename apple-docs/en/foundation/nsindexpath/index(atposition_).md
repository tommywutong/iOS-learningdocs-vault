---
title: 'index(atPosition:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/index(atposition:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/index(atposition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/index%28atposition%3A%29.json'
content_hash: 'sha256:27c0bb256fe558a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# index(atPosition:)

<sub>Instance Method</sub>

Provides the value at a particular node in the index path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(atPosition position: Int) -> Int
```

## Parameters

- `position` — Index value of the desired node. Node numbering starts at zero.

## Return Value

The index value at `node` or `NSNotFound` if the node is outside the range of the index path.

## See Also

### Working with Indexes

- [- getIndexes:range:](<getindexes(__range_).md>) — Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.
- [- getIndexes:](<getindexes(__).md>) — Copies the objects contained in the index path into indexes. _(deprecated)_

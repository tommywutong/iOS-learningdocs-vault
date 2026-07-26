---
title: 'getIndexes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsindexpath/getindexes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/getindexes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/getindexes%28_%3A%29.json'
content_hash: 'sha256:4fa075204375b7f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# getIndexes(_:)

<sub>Instance Method</sub>

Copies the objects contained in the index path into indexes.

> [!warning] Deprecated
> Use [- getIndexes:range:](<getindexes(__range_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getIndexes(_ indexes: UnsafeMutablePointer<Int>)
```

## Parameters

- `indexes` — Pointer to a C array of objects of size at least the length of the index path. On return, the index path’s indexes.

## Discussion

You must allocate the memory for the C array.

## See Also

### Working with Indexes

- [- indexAtPosition:](<index(atposition_).md>) — Provides the value at a particular node in the index path.
- [- getIndexes:range:](<getindexes(__range_).md>) — Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.

---
title: 'getIndexes(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexpath/getindexes(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexpath/getindexes(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexpath/getindexes%28_%3Arange%3A%29.json'
content_hash: 'sha256:96550b01c1b26c30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexPath](../nsindexpath.md)

# getIndexes(_:range:)

<sub>Instance Method</sub>

Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getIndexes(_ indexes: UnsafeMutablePointer<Int>, range positionRange: NSRange)
```

## Parameters

- `indexes` — Pointer to a C array of at least as many [NSUInteger](../../objectivec/nsuinteger.md) objects as specified by the length of `positionRange`. On return, the array holds the index path’s indexes.

- `positionRange` — A range of valid positions within the index path. If the location plus the length of `positionRange` is greater than the length of the index path, this method raises an [NSRangeException](../nsexceptionname/rangeexception.md).

## Discussion

You must allocate the memory for the C array.

## See Also

### Working with Indexes

- [- indexAtPosition:](<index(atposition_).md>) — Provides the value at a particular node in the index path.
- [- getIndexes:](<getindexes(__).md>) — Copies the objects contained in the index path into indexes. _(deprecated)_

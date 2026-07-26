---
title: lastIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexset/lastindex
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/lastindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/lastindex.json'
content_hash: 'sha256:359f0bf58db0d2fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# lastIndex

<sub>Instance Property</sub>

The last index in the index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lastIndex: Int { get }
```

## Discussion

Last index in the index set or NSNotFound when the index set is empty.

## See Also

### Getting Indexes

- [firstIndex](firstindex.md) — The first index in the index set.
- [- indexLessThanIndex:](<indexlessthanindex(__).md>) — Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [- indexLessThanOrEqualToIndex:](<indexlessthanorequal(to_).md>) — Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanOrEqualToIndex:](<indexgreaterthanorequal(to_).md>) — Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanIndex:](<indexgreaterthanindex(__).md>) — Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [- getIndexes:maxCount:inIndexRange:](<getindexes(__maxcount_inindexrange_).md>) — The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.

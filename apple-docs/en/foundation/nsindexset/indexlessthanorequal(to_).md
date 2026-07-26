---
title: 'indexLessThanOrEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/indexlessthanorequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/indexlessthanorequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/indexlessthanorequal%28to%3A%29.json'
content_hash: 'sha256:eb8285fb39ee06a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# indexLessThanOrEqual(to:)

<sub>Instance Method</sub>

Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexLessThanOrEqual(to value: Int) -> Int
```

## Parameters

- `value` — Index being inquired about.

## Return Value

Closest index in the index set less than or equal to `index`; NSNotFound when the index set contains no qualifying index.

## See Also

### Getting Indexes

- [firstIndex](firstindex.md) — The first index in the index set.
- [lastIndex](lastindex.md) — The last index in the index set.
- [- indexLessThanIndex:](<indexlessthanindex(__).md>) — Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [- indexGreaterThanOrEqualToIndex:](<indexgreaterthanorequal(to_).md>) — Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanIndex:](<indexgreaterthanindex(__).md>) — Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [- getIndexes:maxCount:inIndexRange:](<getindexes(__maxcount_inindexrange_).md>) — The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.

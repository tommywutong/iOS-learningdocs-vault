---
title: 'getIndexes(_:maxCount:inIndexRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/getindexes(_:maxcount:inindexrange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/getindexes(_:maxcount:inindexrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/getindexes%28_%3Amaxcount%3Ainindexrange%3A%29.json'
content_hash: 'sha256:8d44e704a779842a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# getIndexes(_:maxCount:inIndexRange:)

<sub>Instance Method</sub>

The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getIndexes(_ indexBuffer: UnsafeMutablePointer<Int>, maxCount bufferSize: Int, inIndexRange range: NSRangePointer?) -> Int
```

## Parameters

- `indexBuffer` — Index buffer to fill.

- `bufferSize` — Maximum size of `indexBuffer`.

- `range` — Index range to compare with indexes in the index set; `nil` represents all the indexes in the index set. Indexes in the index range and in the index set are copied to `indexBuffer`. On output, the range of indexes not copied to `indexBuffer`.

## Return Value

Number of indexes placed in `indexBuffer`.

## Discussion

You are responsible for allocating the memory required for `indexBuffer` and for releasing it later.

Suppose you have an index set with contiguous indexes from 1 to 100. If you use this method to request a range of `(1, 100)`—which represents the set of indexes 1 through 100—and specify a buffer size of `20`, this method returns 20 indexes—1 through 20—in `indexBuffer` and sets `indexRange` to `(21, 80)`—which represents the indexes 21 through 100.

Use this method to retrieve entries quickly and efficiently from an index set. You can call this method repeatedly to retrieve blocks of index values and then process them. When doing so, use the return value and `indexRange` to determine when you have finished processing the desired indexes. When the return value is less than `bufferSize`, you have reached the end of the range.

## See Also

### Getting Indexes

- [firstIndex](firstindex.md) — The first index in the index set.
- [lastIndex](lastindex.md) — The last index in the index set.
- [- indexLessThanIndex:](<indexlessthanindex(__).md>) — Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [- indexLessThanOrEqualToIndex:](<indexlessthanorequal(to_).md>) — Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanOrEqualToIndex:](<indexgreaterthanorequal(to_).md>) — Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [- indexGreaterThanIndex:](<indexgreaterthanindex(__).md>) — Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.

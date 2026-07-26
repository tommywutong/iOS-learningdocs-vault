---
title: 'replaceObjects(at:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/replaceobjects(at:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobjects(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/replaceobjects%28at%3Awith%3A%29.json'
content_hash: 'sha256:48a7361effcdd29c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# replaceObjects(at:with:)

<sub>Instance Method</sub>

Replaces the objects in the receiving array at locations specified with the objects from a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceObjects(at indexes: IndexSet, with objects: [Any])
```

## Parameters

- `indexes` — The indexes of the objects to be replaced.

- `objects` — The objects with which to replace the objects in the receiving array at the indexes specified by `indexes`. The count of locations in `indexes` must equal the count of `objects`.

## Discussion

The indexes in `indexes` are used in the same order as the objects in `objects`.

If `objects` or `indexes` is `nil`, this method raises an exception.

## See Also

### Related Documentation

- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.

### Replacing Objects

- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at `index` with `anObject`.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- replaceObjectsInRange:withObjectsFromArray:](<replaceobjects(in_withobjectsfrom_).md>) — Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [- setArray:](<setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

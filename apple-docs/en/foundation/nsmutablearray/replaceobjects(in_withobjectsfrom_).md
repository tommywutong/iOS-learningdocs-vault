---
title: 'replaceObjects(in:withObjectsFrom:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/replaceobjects(in:withobjectsfrom:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobjects(in:withobjectsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/replaceobjects%28in%3Awithobjectsfrom%3A%29.json'
content_hash: 'sha256:0294e48341d315f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# replaceObjects(in:withObjectsFrom:)

<sub>Instance Method</sub>

Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceObjects(in range: NSRange, withObjectsFrom otherArray: [Any])
```

## Parameters

- `range` — The range of objects to be replaced in (or removed from) the receiving array.

- `otherArray` — The array of objects from which to select replacements for the objects in `aRange`.

## Discussion

If `otherArray` has fewer objects than are specified by `aRange`, the extra objects in the receiving array are removed. If `otherArray` has more objects than are specified by `aRange`, the extra objects from `otherArray` are inserted into the receiving array.

## See Also

### Related Documentation

- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.

### Replacing Objects

- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at `index` with `anObject`.
- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- setArray:](<setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

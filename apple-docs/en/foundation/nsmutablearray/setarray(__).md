---
title: 'setArray(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/setarray(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/setarray(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/setarray%28_%3A%29.json'
content_hash: 'sha256:e824e341d422cb13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# setArray(_:)

<sub>Instance Method</sub>

Sets the receiving array’s elements to those in another given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setArray(_ otherArray: [Any])
```

## Parameters

- `otherArray` — The array of objects with which to replace the receiving array’s content.

## See Also

### Related Documentation

- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds the objects contained in another given array to the end of the receiving array’s content.

### Replacing Objects

- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at `index` with `anObject`.
- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- replaceObjectsInRange:withObjectsFromArray:](<replaceobjects(in_withobjectsfrom_).md>) — Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.

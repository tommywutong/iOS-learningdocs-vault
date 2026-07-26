---
title: 'replaceObject(at:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/replaceobject(at:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/replaceobject(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/replaceobject%28at%3Awith%3A%29.json'
content_hash: 'sha256:8b459e70f3da936a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# replaceObject(at:with:)

<sub>Instance Method</sub>

Replaces the object at `index` with `anObject`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceObject(at index: Int, with anObject: Any)
```

## Parameters

- `index` — The index of the object to be replaced. This value must not exceed the bounds of the array. > [!important] Important > Raises an `NSRangeException` if `index` is beyond the end of the array.

- `anObject` — The object with which to replace the object at index `index` in the array. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `anObject` is `nil`.

## See Also

### Related Documentation

- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.

### Replacing Objects

- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- replaceObjectsInRange:withObjectsFromArray:](<replaceobjects(in_withobjectsfrom_).md>) — Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [- setArray:](<setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

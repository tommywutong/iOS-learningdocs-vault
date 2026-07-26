---
title: 'setObject:atIndexedSubscript:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:b8b41f22defc1af6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Replaces the object at the index with the new object, possibly adding the object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setObject:(ObjectType) obj atIndexedSubscript:(NSUInteger) idx;
```

## Parameters

- `obj` — The object with which to replace the object at index `idx` in the array. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `anObject` is `nil`.

- `idx` — The index of the object to be replaced. This value must not exceed the bounds of the array. > [!important] Important > Raises an `NSRangeException` if `idx` is beyond the end of the array.

## Discussion

This method has the same behavior as the [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) method.

If `idx` is beyond the end of the array (that is, if `idx` is greater than the value returned by `count`), an [NSRangeException](../nsexceptionname/rangeexception.md) is raised.

You shouldn’t need to call this method directly. Instead, this method is called when setting an object by index using subscripting.

```objc
mutableArray[3] = @"someValue"; // equivalent to [mutableArray replaceObjectAtIndex:3 withObject:@"someValue"]
```

## See Also

### Related Documentation

- [- objectAtIndexedSubscript:](<../nsarray/subscript(__).md>) — Returns the object at the specified index.
- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.
- [- removeObjectAtIndex:](<removeobject(at_).md>) — Removes the object at `index` .
- [- removeObjectsAtIndexes:](<removeobjects(at_).md>) — Removes the objects at the specified indexes from the array.

### Replacing Objects

- [- replaceObjectAtIndex:withObject:](<replaceobject(at_with_).md>) — Replaces the object at `index` with `anObject`.
- [- replaceObjectsAtIndexes:withObjects:](<replaceobjects(at_with_).md>) — Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [- replaceObjectsInRange:withObjectsFromArray:range:](<replaceobjects(in_withobjectsfrom_range_).md>) — Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [- replaceObjectsInRange:withObjectsFromArray:](<replaceobjects(in_withobjectsfrom_).md>) — Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [- setArray:](<setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

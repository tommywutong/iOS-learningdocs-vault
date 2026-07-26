---
title: 'getObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsarray/getobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/getobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/getobjects%3A.json'
content_hash: 'sha256:1a2269bb0ec35f4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# getObjects:

<sub>Instance Method</sub>

Copies all the objects contained in the array to `aBuffer`.

> [!warning] Deprecated
> Use [getObjects:range:](getobjects_range_.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) getObjects:(ObjectType[]) objects;
```

## Parameters

- `objects` — A C array of objects of size at least the count of the array.

## Discussion

The method copies into `aBuffer` all the objects in the array; the size of the buffer must therefore be at least the count of the array multiplied by the size of an object reference, as shown in the following example (note that this is just an example, you should typically not create a buffer simply to iterate over the contents of an array):

```objc
NSArray *mArray = // ...;
id *objects;
 
NSUInteger count = [mArray count];
objects = malloc(sizeof(id) * count);
 
[mArray getObjects:objects];
 
for (i = 0; i < count; i++) {
    NSLog(@"object at index %d: %@", i, objects[i]);
}
free(objects);
```

### Special Considerations

This deprecated method is unsafe because it could potentially cause buffer overruns.

## See Also

### Related Documentation

- [+ arrayWithObjects:count:](<init(objects_count_)-7dct1.md>) — Creates and returns an array that includes a given number of objects from a given C array.

### Querying an Array

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.
- [count](count.md) — The number of objects in the array.
- [getObjects:range:](getobjects_range_.md) — Copies references to objects contained in the array that fall within the specified range to `aBuffer`.
- [firstObject](firstobject.md) — The first object in the array.
- [lastObject](lastobject.md) — The last object in the array.
- [- objectAtIndex:](<object(at_).md>) — Returns the object located at the specified index.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns an array containing the objects in the array at the indexes specified by a given index set.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the array.
- [- reverseObjectEnumerator](<reverseobjectenumerator().md>) — Returns an enumerator object that lets you access each object in the array, in reverse order.

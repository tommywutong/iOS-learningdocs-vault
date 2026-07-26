---
title: 'objects(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/objects(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/objects(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/objects%28at%3A%29.json'
content_hash: 'sha256:f6ba6e20fc23d88c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# objects(at:)

<sub>Instance Method</sub>

Returns the objects in the ordered set at the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objects(at indexes: IndexSet) -> [Any]
```

## Parameters

- `indexes` — The indexes.

## Return Value

The returned objects are in the ascending order of their indexes in indexes, so that object in returned ordered set with higher index in indexes will follow the object with smaller index in indexes.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any location in indexes exceeds the bounds of the array, of if `indexes` is `nil`.

## See Also

### Accessing Set Members

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the ordered set at the specified indexes.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the ordered set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [firstObject](firstobject.md) — The first object in the ordered set.
- [lastObject](lastobject.md) — The last object in the ordered set.
- [- objectAtIndex:](<object(at_).md>) — Returns the object at the specified index of the set.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index of the set.
- [- indexOfObject:](<index(of_).md>) — Returns the index of the specified object.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [- indexOfObjectAtIndexes:options:passingTest:](<index(ofobjectat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectPassingTest:](<index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexes(ofobjectspassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.

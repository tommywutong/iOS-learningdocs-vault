---
title: lastObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedset/lastobject
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/lastobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/lastobject.json'
content_hash: 'sha256:d319770bb4741798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# lastObject

<sub>Instance Property</sub>

The last object in the ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lastObject: Any? { get }
```

## See Also

### Accessing Set Members

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the ordered set.
- [- enumerateObjectsAtIndexes:options:usingBlock:](<enumerateobjects(at_options_using_).md>) — Executes a given block using the objects in the ordered set at the specified indexes.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the ordered set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [firstObject](firstobject.md) — The first object in the ordered set.
- [- objectAtIndex:](<object(at_).md>) — Returns the object at the specified index of the set.
- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the object at the specified index of the set.
- [- objectsAtIndexes:](<objects(at_).md>) — Returns the objects in the ordered set at the specified indexes.
- [- indexOfObject:](<index(of_).md>) — Returns the index of the specified object.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [- indexOfObjectAtIndexes:options:passingTest:](<index(ofobjectat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectPassingTest:](<index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexes(ofobjectspassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.

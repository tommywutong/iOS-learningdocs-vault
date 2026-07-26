---
title: 'indexes(options:ofObjectsPassingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/indexes(options:ofobjectspassingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/indexes(options:ofobjectspassingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/indexes%28options%3Aofobjectspassingtest%3A%29.json'
content_hash: 'sha256:d4180e660087227a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# indexes(options:ofObjectsPassingTest:)

<sub>Instance Method</sub>

Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexes(options opts: NSEnumerationOptions = [], ofObjectsPassingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet
```

## Parameters

- `opts` — A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).

- `predicate` — The block to apply to elements in the ordered set. The block takes three arguments: - **obj** — The element in the ordered set. - **Term** — The index of the element in the ordered set. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this value to [true](../../swift/true.md) within the block.

## Return Value

The index whose corresponding value in the ordered set passes the test specified by `predicate` and `opts`. If the `opts` bitmask specifies reverse order, then the last item that matches is returned. Otherwise, the index of the first matching object is returned. If no objects in the ordered set pass the test, returns `NSNotFound`.

## Discussion

By default, the enumeration starts with the first object and continues serially through the ordered set to the last object. You can specify [NSEnumerationConcurrent](../nsenumerationoptions/concurrent.md) and/or [NSEnumerationReverse](../nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

> [!important] Important
> If the block parameter or `s` is `nil`, this method raises an exception.

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
- [- objectsAtIndexes:](<objects(at_).md>) — Returns the objects in the ordered set at the specified indexes.
- [- indexOfObject:](<index(of_).md>) — Returns the index of the specified object.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.
- [- indexOfObjectAtIndexes:options:passingTest:](<index(ofobjectat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectPassingTest:](<index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.

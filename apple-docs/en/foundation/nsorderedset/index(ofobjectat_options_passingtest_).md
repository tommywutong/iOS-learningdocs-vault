---
title: 'index(ofObjectAt:options:passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/index(ofobjectat:options:passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/index(ofobjectat:options:passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/index%28ofobjectat%3Aoptions%3Apassingtest%3A%29.json'
content_hash: 'sha256:6ba31f56e155ea17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# index(ofObjectAt:options:passingTest:)

<sub>Instance Method</sub>

Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(ofObjectAt s: IndexSet, options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int
```

## Parameters

- `s` — The indexes of the objects over which to enumerate.

- `opts` — A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).

- `predicate` — The block to apply to elements in the ordered set. The block takes three arguments: - **obj** — The element in the ordered set. - **idx** — The index of the element in the ordered set. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this value to [true](../../swift/true.md) within the block. The block returns a Boolean value that indicates whether `obj` passed the test.

## Return Value

The index of the corresponding value in the ordered set passes the test specified by predicate. If no objects in the ordered set pass the test, returns `NSNotFound`.

## Discussion

By default, the enumeration starts with the first object and continues serially through the ordered set to the last element specified by `s`. You can specify [NSEnumerationConcurrent](../nsenumerationoptions/concurrent.md) and/or [NSEnumerationReverse](../nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

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
- [- indexOfObjectPassingTest:](<index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexes(ofobjectspassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.

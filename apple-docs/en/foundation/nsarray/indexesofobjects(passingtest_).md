---
title: 'indexesOfObjects(passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/indexesofobjects(passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/indexesofobjects(passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/indexesofobjects%28passingtest%3A%29.json'
content_hash: 'sha256:acb0f7e40c91ca24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# indexesOfObjects(passingTest:)

<sub>Instance Method</sub>

Returns the indexes of objects in the array that pass a test in a given block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexesOfObjects(passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet
```

## Parameters

- `predicate` — The block to apply to elements in the array. The block takes three arguments: - **obj** — The element in the array. - **idx** — The index of the element in the array. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further enumeration of the array. If a block stops further enumeration, that block continues to run until it’s finished. The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the block. The block returns a Boolean value that indicates whether `obj` passed the test.

## Return Value

The indexes whose corresponding values in the array pass the test specified by `predicate`. If no objects in the array pass the test, returns an empty index set.

## See Also

### Finding Objects in an Array

- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.
- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectIdenticalTo:inRange:](<indexofobjectidentical(to_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectPassingTest:](<indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectAtIndexes:options:passingTest:](<indexofobject(at_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsWithOptions:passingTest:](<indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

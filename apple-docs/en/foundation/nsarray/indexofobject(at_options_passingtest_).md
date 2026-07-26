---
title: 'indexOfObject(at:options:passingTest:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/indexofobject(at:options:passingtest:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/indexofobject(at:options:passingtest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/indexofobject%28at%3Aoptions%3Apassingtest%3A%29.json'
content_hash: 'sha256:f3e32de13ca40c27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# indexOfObject(at:options:passingTest:)

<sub>Instance Method</sub>

Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexOfObject(at s: IndexSet, options opts: NSEnumerationOptions = [], passingTest predicate: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int
```

## Parameters

- `s` — The indexes of the objects over which to enumerate.

- `opts` — A bit mask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).

- `predicate` — The block to apply to elements in the array. The block takes three arguments: - **obj** — The element in the array. - **idx** — The index of the element in the array. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further enumeration of the array. If a block stops further enumeration, that block continues to run until it’s finished. When the `NSEnumerationConcurrent` enumeration option is specified, enumeration stops after all of the currently running blocks finish. The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the block. The block returns a Boolean value that indicates whether `obj` passed the test.

## Return Value

The lowest index whose corresponding value in the array passes the test specified by `predicate`. If no objects in the array pass the test, returns `NSNotFound`.

## Discussion

By default, the enumeration starts with the first object and continues serially through the array to the last element specified by `indexSet`. You can specify [NSEnumerationConcurrent](../nsenumerationoptions/concurrent.md) and/or [NSEnumerationReverse](../nsenumerationoptions/reverse.md) as enumeration options to modify this behavior.

> [!important] Important
> If the block parameter or `indexSet` is `nil` this method will raise an exception.

## See Also

### Finding Objects in an Array

- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.
- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectIdenticalTo:inRange:](<indexofobjectidentical(to_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectPassingTest:](<indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexesofobjects(passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

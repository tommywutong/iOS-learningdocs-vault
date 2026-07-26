---
title: 'index(of:inSortedRange:options:usingComparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/index(of:insortedrange:options:usingcomparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/index(of:insortedrange:options:usingcomparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/index%28of%3Ainsortedrange%3Aoptions%3Ausingcomparator%3A%29.json'
content_hash: 'sha256:365700d349962bfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# index(of:inSortedRange:options:usingComparator:)

<sub>Instance Method</sub>

Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(of obj: Any, inSortedRange r: NSRange, options opts: NSBinarySearchingOptions = [], usingComparator cmp: (Any, Any) -> ComparisonResult) -> Int
```

## Parameters

- `obj` — An object for which to search in the array. If this value is `nil`, throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md).

- `r` — The range within the array to search for `obj`. If `r` exceeds the bounds of the array (if the location plus length of the range is greater than the count of the array), throws an [NSRangeException](../nsexceptionname/rangeexception.md).

- `opts` — Options for the search. For possible values, see [NSBinarySearchingOptions](../nsbinarysearchingoptions.md). If you specify both [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) and [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md), throws an `NSInvalidArgumentException`.

- `cmp` — A comparator block used to compare the object `obj` with elements in the array. If this value is `NULL`, throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md).

## Return Value

If the [NSBinarySearchingInsertionIndex](../nsbinarysearchingoptions/insertionindex.md) option is not specified:

- If the `obj` is found and neither [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) nor [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) is specified, returns an arbitrary matching object’s index.
- If the [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) option is also specified, returns the lowest index of equal objects.
- If the [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the highest index of equal objects.
- If the object is not found, returns `NSNotFound`.

If the [NSBinarySearchingInsertionIndex](../nsbinarysearchingoptions/insertionindex.md) option is specified, returns the index at which you should insert `obj` in order to maintain a sorted array:

- If the `obj` is found and neither [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) nor [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) is specified, returns any equal or one larger index than any matching object’s index.
- If the [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) option is also specified, returns the lowest index of equal objects.
- If the [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the highest index of equal objects.
- If the object is not found, returns the index of the least greater object, or the index at the end of the array if the object is larger than all other elements.

## Discussion

The elements in the array must have already been sorted using the comparator `cmp`.  If the array is not sorted, the result is undefined.

## See Also

### Finding Objects in an Array

- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.
- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectIdenticalTo:inRange:](<indexofobjectidentical(to_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectPassingTest:](<indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectAtIndexes:options:passingTest:](<indexofobject(at_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexesofobjects(passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.

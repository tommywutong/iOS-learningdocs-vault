---
title: 'index(of:inSortedRange:options:usingComparator:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/index(of:insortedrange:options:usingcomparator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/index(of:insortedrange:options:usingcomparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/index%28of%3Ainsortedrange%3Aoptions%3Ausingcomparator%3A%29.json'
content_hash: 'sha256:a40fb393803ba705'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# index(of:inSortedRange:options:usingComparator:)

<sub>Instance Method</sub>

Returns the index, within a specified range, of an object compared with elements in the ordered set using a given NSComparator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(of object: Any, inSortedRange range: NSRange, options opts: NSBinarySearchingOptions = [], usingComparator cmp: (Any, Any) -> ComparisonResult) -> Int
```

## Parameters

- `object` — An object for which to search in the ordered set. If this value is `nil`, throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md).

- `range` — The range within the array to search for `object`. If r exceeds the bounds of the ordered set (if the location plus length of the range is greater than the count of the ordered set), throws an [NSRangeException](../nsexceptionname/rangeexception.md).

- `opts` — Options for the search. For possible values, see [NSBinarySearchingOptions](../nsbinarysearchingoptions.md).

- `cmp` — A comparator block used to compare the object obj with elements in the ordered set. If this value is `NULL`, throws an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md).

## Return Value

If the [NSBinarySearchingInsertionIndex](../nsbinarysearchingoptions/insertionindex.md) option is not specified:

- If the `object` is found and neither [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) nor [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) or [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of equal objects.
- If the object is not found, returns `NSNotFound`.

If the [NSBinarySearchingInsertionIndex](../nsbinarysearchingoptions/insertionindex.md) option is specified, returns the index at which you should insert `obj` in order to maintain a sorted array:

- If the `object` is found and neither [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) nor [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) is specified, returns the matching object’s index.
- If the [NSBinarySearchingFirstEqual](../nsbinarysearchingoptions/firstequal.md) or  [NSBinarySearchingLastEqual](../nsbinarysearchingoptions/lastequal.md) option is also specified, returns the index of the equal objects.
- If the object is not found, returns the index of the least greater object, or the index at the end of the array if the object is larger than all other elements.

## Discussion

The elements in the ordered set  must have already been sorted using the comparator `cmp`. If the ordered set is not sorted, the result is undefined.

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
- [- indexOfObjectAtIndexes:options:passingTest:](<index(ofobjectat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectPassingTest:](<index(ofobjectpassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<index(__ofobjectpassingtest_).md>) — Returns the index of an object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexes(ofobjectsat_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the object in the ordered set that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexes(ofobjectspassingtest_).md>) — Returns the index of the object in the ordered set that passes a test in a given block.

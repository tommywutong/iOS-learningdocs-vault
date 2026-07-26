---
title: 'indexOfObjectIdentical(to:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/indexofobjectidentical(to:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/indexofobjectidentical(to:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/indexofobjectidentical%28to%3Ain%3A%29.json'
content_hash: 'sha256:f58bc8da3d2c43b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# indexOfObjectIdentical(to:in:)

<sub>Instance Method</sub>

Returns the lowest index within a specified range whose corresponding array value is equal to a given object .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indexOfObjectIdentical(to anObject: Any, in range: NSRange) -> Int
```

## Parameters

- `anObject` — An object.

- `range` — The range of indexes in the array within which to search for `anObject`.

## Return Value

The lowest index within `range` whose corresponding array value is identical to `anObject`. If none of the objects within `range` is identical to `anObject`, returns `NSNotFound`.

## Discussion

Objects are considered identical if their object addresses are the same.

## See Also

### Related Documentation

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.

### Finding Objects in an Array

- [- indexOfObject:](<index(of_).md>) — Returns the lowest index whose corresponding array value is equal to a given object.
- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectPassingTest:](<indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectAtIndexes:options:passingTest:](<indexofobject(at_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexesofobjects(passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

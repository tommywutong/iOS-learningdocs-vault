---
title: 'index(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/index(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/index(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/index%28of%3A%29.json'
content_hash: 'sha256:9fad200fd1149701'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# index(of:)

<sub>Instance Method</sub>

Returns the lowest index whose corresponding array value is equal to a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(of anObject: Any) -> Int
```

## Parameters

- `anObject` — An object.

## Return Value

The lowest index whose corresponding array value is equal to `anObject`. If none of the objects in the array is equal to `anObject`, returns `NSNotFound`.

## Discussion

Starting at index `0`, each element of the array is passed as an argument to an [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) message sent to `anObject` until a match is found or the end of the array is reached. Objects are considered equal if [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) (declared in the [NSObjectProtocol](../../objectivec/nsobjectprotocol.md) protocol) returns [true](../../swift/true.md).

## See Also

### Related Documentation

- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the array.

### Finding Objects in an Array

- [- indexOfObject:inRange:](<index(of_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectIdenticalTo:](<indexofobjectidentical(to_).md>) — Returns the lowest index whose corresponding array value is identical to a given object.
- [- indexOfObjectIdenticalTo:inRange:](<indexofobjectidentical(to_in_).md>) — Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [- indexOfObjectPassingTest:](<indexofobject(passingtest_).md>) — Returns the index of the first object in the array that passes a test in a given block.
- [- indexOfObjectWithOptions:passingTest:](<indexofobject(options_passingtest_).md>) — Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexOfObjectAtIndexes:options:passingTest:](<indexofobject(at_options_passingtest_).md>) — Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsPassingTest:](<indexesofobjects(passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block.
- [- indexesOfObjectsWithOptions:passingTest:](<indexesofobjects(options_passingtest_).md>) — Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexesOfObjectsAtIndexes:options:passingTest:](<indexesofobjects(at_options_passingtest_).md>) — Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [- indexOfObject:inSortedRange:options:usingComparator:](<index(of_insortedrange_options_usingcomparator_).md>) — Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.

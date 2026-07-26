---
title: 'orderedSetWithArray:range:copyItems:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/orderedsetwitharray:range:copyitems:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetwitharray:range:copyitems:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/orderedsetwitharray%3Arange%3Acopyitems%3A.json'
content_hash: 'sha256:c94e4e888d7f3646'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# orderedSetWithArray:range:copyItems:

<sub>Type Method</sub>

Creates and returns a new ordered set for a specified range of objects in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) orderedSetWithArray:(NSArray<id> *) array range:(NSRange) range copyItems:(BOOL) flag;
```

## Parameters

- `array` — The array

- `range` — The range of the objects to add to the ordered set.

- `flag` — If [true](../../swift/true.md) the objects are copied to the ordered set; otherwise [false](../../swift/false.md).

## Return Value

A new ordered set containing a uniqued collection of the objects contained in the specified range of the array.

## See Also

### Related Documentation

- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithArray:range:copyItems:](<init(array_range_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.

### Creating an Ordered Set

- [orderedSet](orderedset.md) — Creates and returns an empty ordered set
- [orderedSetWithArray:](orderedsetwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [orderedSetWithObject:](orderedsetwithobject_.md) — Creates and returns a ordered set that contains a single given object.
- [orderedSetWithObjects:](orderedsetwithobjects_.md) — Creates and returns a ordered set containing the objects in a given argument list.
- [+ orderedSetWithObjects:count:](<init(objects_count_)-3ny0m.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [orderedSetWithOrderedSet:](orderedsetwithorderedset_.md) — Creates and returns an ordered set containing the objects from another ordered set.
- [orderedSetWithOrderedSet:range:copyItems:](orderedsetwithorderedset_range_copyitems_.md) — Creates and returns a new ordered set for a specified range of objects in an ordered set.
- [orderedSetWithSet:](orderedsetwithset_.md) — Creates and returns an ordered set with the contents of a set.
- [orderedSetWithSet:copyItems:](orderedsetwithset_copyitems_.md) — Creates and returns an ordered set with the contents of a set, optionally copying the items.

---
title: 'orderedSetWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/orderedsetwithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetwithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/orderedsetwithobjects%3A.json'
content_hash: 'sha256:4e0cfa3ede614a18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# orderedSetWithObjects:

<sub>Type Method</sub>

Creates and returns a ordered set containing the objects in a given argument list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) orderedSetWithObjects:(ObjectType) firstObj;
```

## Parameters

- `firstObj` — The first object to add to the new set. If the same object appears more than once in the list of objects, it is added only once to the returned set. The objects are added to the ordered set in the order that they are listed.

## Return Value

A new ordered set containing the objects in the argument list.

## Discussion

To add additional objects to the new set, pass a comma-separated list of trailing variadic arguments, ending with `nil`.

## See Also

### Related Documentation

- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.

### Creating an Ordered Set

- [orderedSet](orderedset.md) — Creates and returns an empty ordered set
- [orderedSetWithArray:](orderedsetwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [orderedSetWithArray:range:copyItems:](orderedsetwitharray_range_copyitems_.md) — Creates and returns a new ordered set for a specified range of objects in an array.
- [orderedSetWithObject:](orderedsetwithobject_.md) — Creates and returns a ordered set that contains a single given object.
- [+ orderedSetWithObjects:count:](<init(objects_count_)-3ny0m.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [orderedSetWithOrderedSet:](orderedsetwithorderedset_.md) — Creates and returns an ordered set containing the objects from another ordered set.
- [orderedSetWithOrderedSet:range:copyItems:](orderedsetwithorderedset_range_copyitems_.md) — Creates and returns a new ordered set for a specified range of objects in an ordered set.
- [orderedSetWithSet:](orderedsetwithset_.md) — Creates and returns an ordered set with the contents of a set.
- [orderedSetWithSet:copyItems:](orderedsetwithset_copyitems_.md) — Creates and returns an ordered set with the contents of a set, optionally copying the items.

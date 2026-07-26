---
title: 'orderedSetWithOrderedSet:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/orderedsetwithorderedset:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetwithorderedset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/orderedsetwithorderedset%3A.json'
content_hash: 'sha256:29cbc512a7bb96a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# orderedSetWithOrderedSet:

<sub>Type Method</sub>

Creates and returns an ordered set containing the objects from another ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) orderedSetWithOrderedSet:(NSOrderedSet<id> *) set;
```

## Parameters

- `set` — A set containing the objects to add to the new ordered set. The objects are not copied, simply referenced.

## Return Value

A new ordered set containing the objects from set.

## See Also

### Related Documentation

- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:range:copyItems:](<init(orderedset_range_copyitems_).md>) — Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.

### Creating an Ordered Set

- [orderedSet](orderedset.md) — Creates and returns an empty ordered set
- [orderedSetWithArray:](orderedsetwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [orderedSetWithArray:range:copyItems:](orderedsetwitharray_range_copyitems_.md) — Creates and returns a new ordered set for a specified range of objects in an array.
- [orderedSetWithObject:](orderedsetwithobject_.md) — Creates and returns a ordered set that contains a single given object.
- [orderedSetWithObjects:](orderedsetwithobjects_.md) — Creates and returns a ordered set containing the objects in a given argument list.
- [+ orderedSetWithObjects:count:](<init(objects_count_)-3ny0m.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [orderedSetWithOrderedSet:range:copyItems:](orderedsetwithorderedset_range_copyitems_.md) — Creates and returns a new ordered set for a specified range of objects in an ordered set.
- [orderedSetWithSet:](orderedsetwithset_.md) — Creates and returns an ordered set with the contents of a set.
- [orderedSetWithSet:copyItems:](orderedsetwithset_copyitems_.md) — Creates and returns an ordered set with the contents of a set, optionally copying the items.

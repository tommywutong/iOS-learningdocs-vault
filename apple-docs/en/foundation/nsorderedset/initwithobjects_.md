---
title: 'initWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/initwithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/initwithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/initwithobjects%3A.json'
content_hash: 'sha256:5cc5433d375905d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# initWithObjects:

<sub>Instance Method</sub>

Initializes a newly allocated set with members taken from the specified list of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithObjects:(ObjectType) firstObj;
```

## Parameters

- `firstObj` — The first object to add to the new set.

## Return Value

An initialized ordered set containing the objects specified in the parameter list. The returned set might be different than the original receiver.

## Discussion

To add additional objects to the new ordered set, pass comma-separated list of trailing variadic arguments, ending with `nil`,

```
If the same object appears more than once in the list, it is represented only once in the returned ordered set. 
```

## See Also

### Related Documentation

- [orderedSetWithObjects:](orderedsetwithobjects_.md) — Creates and returns a ordered set containing the objects in a given argument list.
- [orderedSetWithObject:](orderedsetwithobject_.md) — Creates and returns a ordered set that contains a single given object.

### Initializing an Ordered Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [- initWithArray:range:copyItems:](<init(array_range_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [- initWithObject:](<init(object_).md>) — Initializes a new ordered set with the object.
- [- initWithObjects:count:](<init(objects_count_)-2ai32.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:range:copyItems:](<init(orderedset_range_copyitems_).md>) — Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [- initWithSet:](<init(set_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [- init](<init().md>) — Initializes a newly allocated ordered set.

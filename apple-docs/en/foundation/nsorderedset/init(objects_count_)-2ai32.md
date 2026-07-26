---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/init(objects:count:)-2ai32'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/init(objects:count:)-2ai32'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/init%28objects%3Acount%3A%29-2ai32.json'
content_hash: 'sha256:2af1029e6c37f65e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# init(objects:count:)

<sub>Initializer</sub>

Initializes a newly allocated set with a specified number of objects from a given C array of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(objects: UnsafePointer<AnyObject>?, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects to add to the new set. If the same object appears more than once in objects, it is added only once to the returned ordered set.

- `cnt` — The number of objects from objects to add to the new ordered set.

## Return Value

An initialized ordered set containing cnt objects from the list of objects specified by objects. The returned set might be different than the original receiver.

## Discussion

This method is a designated initializer of `NSOrderedSet`.

## See Also

### Related Documentation

- [+ orderedSetWithObjects:count:](<init(objects_count_)-3ny0m.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.

### Initializing an Ordered Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [- initWithArray:range:copyItems:](<init(array_range_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [- initWithObject:](<init(object_).md>) — Initializes a new ordered set with the object.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:range:copyItems:](<init(orderedset_range_copyitems_).md>) — Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [- initWithSet:](<init(set_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [- init](<init().md>) — Initializes a newly allocated ordered set.

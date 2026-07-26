---
title: 'init(array:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/init(array:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/init(array:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/init%28array%3A%29.json'
content_hash: 'sha256:5d45b747db9626f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# init(array:)

<sub>Initializer</sub>

Initializes a newly allocated set with the objects that are contained in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(array: [Any])
```

## Parameters

- `array` — An array of objects to add to the new set. If the same object appears more than once in array, it is represented only once in the returned ordered set.

## Return Value

An initialized ordered set with the contents of array. The returned ordered set might be different than the original receiver.

## See Also

### Initializing an Ordered Set

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

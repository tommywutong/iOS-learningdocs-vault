---
title: 'init(object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/init(object:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/init(object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/init%28object%3A%29.json'
content_hash: 'sha256:4e4e438bd128391e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# init(object:)

<sub>Initializer</sub>

Initializes a new ordered set with the object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object: Any)
```

## Parameters

- `object` — The object to add to the new ordered set

## Return Value

A new ordered set that contains a single member, `object`.

## See Also

### Initializing an Ordered Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in a given array, optionally copying the items.
- [- initWithArray:range:copyItems:](<init(array_range_copyitems_).md>) — Initializes a newly allocated set with the objects that are contained in the specified range of an array, optionally copying the items.
- [- initWithObjects:count:](<init(objects_count_)-2ai32.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:range:copyItems:](<init(orderedset_range_copyitems_).md>) — Initializes a new ordered set with the contents of an ordered set, optionally copying the items.
- [- initWithSet:](<init(set_).md>) — Initializes a new ordered set with the contents of a set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the objects in the set.
- [- init](<init().md>) — Initializes a newly allocated ordered set.

---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/init(objects:count:)-3ny0m'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/init(objects:count:)-3ny0m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/init%28objects%3Acount%3A%29-3ny0m.json'
content_hash: 'sha256:7f90fc1d68a8320b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# init(objects:count:)

<sub>Initializer</sub>

Creates and returns a set containing a specified number of objects from a given C array of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(objects: UnsafePointer<AnyObject>, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects to add to the new ordered set. If the same object appears more than once in objects, it is added only once to the returned ordered set. Each object receives a retain message as it is added to the set.

- `cnt` — The number of objects from objects to add to the new set.

## Return Value

A new ordered set containing cnt objects from the list of objects specified by `objects`.

## See Also

### Related Documentation

- [- initWithOrderedSet:copyItems:](<init(orderedset_copyitems_).md>) — Initializes a new ordered set with the contents of a set, optionally copying the items.
- [- initWithOrderedSet:](<init(orderedset_).md>) — Initializes a new ordered set with the contents of a set.

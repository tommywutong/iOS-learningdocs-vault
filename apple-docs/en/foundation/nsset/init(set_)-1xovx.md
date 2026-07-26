---
title: 'init(set:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(set:)-1xovx'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(set:)-1xovx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28set%3A%29-1xovx.json'
content_hash: 'sha256:6997c007eff3bd0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(set:)

<sub>Initializer</sub>

Initializes a newly allocated set and adds to it objects from another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(set: Set<AnyHashable>)
```

## Parameters

- `set` — A set containing objects to add to the receiving set. Each object is retained as it is added.

## Return Value

An initialized objects set containing the objects from `set`. The returned set might be different than the original receiver.

## See Also

### Initializing a Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithObjects:count:](<init(objects_count_)-7kift.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a newly allocated set and adds to it members of another given set.
- [- init](<init().md>) — Initializes a newly allocated set.

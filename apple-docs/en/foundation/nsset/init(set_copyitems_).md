---
title: 'init(set:copyItems:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(set:copyitems:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(set:copyitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28set%3Acopyitems%3A%29.json'
content_hash: 'sha256:48e175789df0b375'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(set:copyItems:)

<sub>Initializer</sub>

Initializes a newly allocated set and adds to it members of another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(set: Set<AnyHashable>, copyItems flag: Bool)
```

## Parameters

- `set` — A set containing objects to add to the new set.

- `flag` — If [true](../../swift/true.md), each object in `set` receives a [copyWithZone:](../../objectivec/nsobject-swift.class/copywithzone_.md) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned set. If [false](../../swift/false.md), then in a managed memory environment each object in `set` simply receives a `retain` message when it is added to the returned set.

## Return Value

An initialized set that contains the members of `set`. The returned set might be different than the original receiver.

## Discussion

After an immutable s has been initialized in this way, it cannot be modified.

The [- copyWithZone:](<../nscopying/copy(with_).md>) method performs a shallow copy. If you have a collection of arbitrary depth, passing [true](../../swift/true.md) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [false](../../swift/false.md) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## See Also

### Initializing a Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithObjects:count:](<init(objects_count_)-7kift.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithSet:](<init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.
- [- init](<init().md>) — Initializes a newly allocated set.

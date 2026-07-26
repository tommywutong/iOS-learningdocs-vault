---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(objects:count:)-7kift'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(objects:count:)-7kift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28objects%3Acount%3A%29-7kift.json'
content_hash: 'sha256:603bbdf72f7a4385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(objects:count:)

<sub>Initializer</sub>

Initializes a newly allocated set with a specified number of objects from a given C array of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(objects: UnsafePointer<AnyObject>?, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects to add to the new set. If the same object appears more than once in `objects`, it is added only once to the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

- `cnt` — The number of objects from `objects` to add to the new set.

## Return Value

An initialized set containing `cnt` objects from the list of objects specified by `objects`. The returned set might be different than the original receiver.

## Discussion

This method is a designated initializer for `NSSet`.

## See Also

### Related Documentation

- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.

### Initializing a Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithSet:](<init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a newly allocated set and adds to it members of another given set.
- [- init](<init().md>) — Initializes a newly allocated set.

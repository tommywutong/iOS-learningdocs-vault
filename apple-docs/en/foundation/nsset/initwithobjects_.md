---
title: 'initWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/initwithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/initwithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/initwithobjects%3A.json'
content_hash: 'sha256:a664a44b107e1129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

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

An initialized set containing the objects specified in the parameter list. The returned set might be different than the original receiver.

## Discussion

To add additional objects to the new set, pass a comma-separated list of trailing variadic arguments, ending with `nil`.  If the same object appears more than once in the list of objects, it is added only once to the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

## See Also

### Related Documentation

- [setWithObjects:](setwithobjects_.md) — Creates and returns a set containing the objects in a given argument list.

### Initializing a Set

- [- initWithArray:](<init(array_).md>) — Initializes a newly allocated set with the objects that are contained in a given array.
- [- initWithObjects:count:](<init(objects_count_)-7kift.md>) — Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [- initWithSet:](<init(set_)-1xovx.md>) — Initializes a newly allocated set and adds to it objects from another given set.
- [- initWithSet:copyItems:](<init(set_copyitems_).md>) — Initializes a newly allocated set and adds to it members of another given set.
- [- init](<init().md>) — Initializes a newly allocated set.

---
title: NSShouldRetainWithZone
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsshouldretainwithzone
source_url: 'https://developer.apple.com/documentation/foundation/nsshouldretainwithzone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsshouldretainwithzone.json'
content_hash: 'sha256:bd33cd1f27297c6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSShouldRetainWithZone

<sub>Function</sub>

Indicates whether an object should be retained.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern BOOL NSShouldRetainWithZone(id anObject, NSZone *requestedZone);
```

## Parameters

- `anObject` — An object.

- `requestedZone` — A memory zone.

## Return Value

Returns [true](../swift/true.md) if `requestedZone` is `NULL`, the default zone, or the zone in which `anObject` was allocated; otherwise [false](../swift/false.md).

## Discussion

This function is typically called from inside an `NSObject`’s [copyWithZone:](../objectivec/nsobject-swift.class/copywithzone_.md), when deciding whether to retain `anObject` as opposed to making a copy of it.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## See Also

### Object Allocation and Deallocation

- [NSAllocateObject](nsallocateobject.md) — Creates and returns a new instance of a given class.
- [NSCopyObject](nscopyobject.md) — Creates an exact copy of an object. _(deprecated)_
- [NSDeallocateObject](nsdeallocateobject.md) — Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSExtraRefCount](nsextrarefcount.md) — Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](nsincrementextrarefcount.md) — Increments the specified object’s reference count.

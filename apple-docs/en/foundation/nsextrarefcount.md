---
title: NSExtraRefCount
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextrarefcount
source_url: 'https://developer.apple.com/documentation/foundation/nsextrarefcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextrarefcount.json'
content_hash: 'sha256:dde23097fd14b1e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExtraRefCount

<sub>Function</sub>

Returns the specified object’s reference count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSUInteger NSExtraRefCount(id object);
```

## Parameters

- `object` — An object.

## Return Value

The current reference count of `object`.

## Discussion

This function is used in conjunction with [NSIncrementExtraRefCount](nsincrementextrarefcount.md) and [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) in situations where you need to override an object’s [retain](../objectivec/nsobject-c.protocol/retain.md) and [release](../objectivec/nsobject-c.protocol/release.md) methods.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## See Also

### Object Allocation and Deallocation

- [NSAllocateObject](nsallocateobject.md) — Creates and returns a new instance of a given class.
- [NSCopyObject](nscopyobject.md) — Creates an exact copy of an object. _(deprecated)_
- [NSDeallocateObject](nsdeallocateobject.md) — Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSIncrementExtraRefCount](nsincrementextrarefcount.md) — Increments the specified object’s reference count.
- [NSShouldRetainWithZone](nsshouldretainwithzone.md) — Indicates whether an object should be retained.

---
title: NSDeallocateObject
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdeallocateobject
source_url: 'https://developer.apple.com/documentation/foundation/nsdeallocateobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdeallocateobject.json'
content_hash: 'sha256:e736cab64471ce4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDeallocateObject

<sub>Function</sub>

Destroys an existing object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void NSDeallocateObject(id object);
```

## Parameters

- `object` — An object.

## Discussion

This function deallocates `object`, which must have been allocated using `NSAllocateObject`.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## See Also

### Object Allocation and Deallocation

- [NSAllocateObject](nsallocateobject.md) — Creates and returns a new instance of a given class.
- [NSCopyObject](nscopyobject.md) — Creates an exact copy of an object. _(deprecated)_
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSExtraRefCount](nsextrarefcount.md) — Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](nsincrementextrarefcount.md) — Increments the specified object’s reference count.
- [NSShouldRetainWithZone](nsshouldretainwithzone.md) — Indicates whether an object should be retained.

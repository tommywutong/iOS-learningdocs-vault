---
title: NSIncrementExtraRefCount
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsincrementextrarefcount
source_url: 'https://developer.apple.com/documentation/foundation/nsincrementextrarefcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsincrementextrarefcount.json'
content_hash: 'sha256:5ab73eebf7f5ebb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIncrementExtraRefCount

<sub>Function</sub>

Increments the specified object’s reference count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void NSIncrementExtraRefCount(id object);
```

## Parameters

- `object` — An object.

## Discussion

This function increments the “extra reference” count of `object`. Newly created objects have only one actual reference, so that a single release message results in the object being deallocated. Extra references are those beyond the single original reference and are usually created by sending the object a retain message. Your code should generally not use these functions unless it is overriding the retain or release methods.

### Special Considerations

This function is deprecated and unavailable for use with ARC.

## See Also

### Object Allocation and Deallocation

- [NSAllocateObject](nsallocateobject.md) — Creates and returns a new instance of a given class.
- [NSCopyObject](nscopyobject.md) — Creates an exact copy of an object. _(deprecated)_
- [NSDeallocateObject](nsdeallocateobject.md) — Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSExtraRefCount](nsextrarefcount.md) — Returns the specified object’s reference count.
- [NSShouldRetainWithZone](nsshouldretainwithzone.md) — Indicates whether an object should be retained.

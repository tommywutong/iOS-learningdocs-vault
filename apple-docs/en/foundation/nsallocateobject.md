---
title: NSAllocateObject
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsallocateobject
source_url: 'https://developer.apple.com/documentation/foundation/nsallocateobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsallocateobject.json'
content_hash: 'sha256:b5145a89c0813ab0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAllocateObject

<sub>Function</sub>

Creates and returns a new instance of a given class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern idNSAllocateObject(Class aClass, NSUInteger extraBytes, NSZone *zone);
```

## Parameters

- `aClass` — The class of which to create an instance.

- `extraBytes` — The number of extra bytes required for indexed instance variables (this value is typically `0`).

- `zone` — The zone in which to create the new instance (pass `NULL` to specify the default zone).

## Return Value

A new instance of `aClass` or `nil` if an instance could not be created.

## Discussion

This function is deprecated and unavailable for use with ARC.

## See Also

### Object Allocation and Deallocation

- [NSCopyObject](nscopyobject.md) — Creates an exact copy of an object. _(deprecated)_
- [NSDeallocateObject](nsdeallocateobject.md) — Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSExtraRefCount](nsextrarefcount.md) — Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](nsincrementextrarefcount.md) — Increments the specified object’s reference count.
- [NSShouldRetainWithZone](nsshouldretainwithzone.md) — Indicates whether an object should be retained.

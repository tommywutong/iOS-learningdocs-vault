---
title: NSCopyObject
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.8 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscopyobject
source_url: 'https://developer.apple.com/documentation/foundation/nscopyobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopyobject.json'
content_hash: 'sha256:74a2d29866f9a441'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCopyObject

<sub>Function</sub>

Creates an exact copy of an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern idNSCopyObject(id object, NSUInteger extraBytes, NSZone *zone);
```

## Parameters

- `object` — The object to copy.

- `extraBytes` — The number of extra bytes required for indexed instance variables (this value is typically `0`).

- `zone` — The zone in which to create the new instance (pass `NULL` to specify the default zone).

## Return Value

A new object that’s an exact copy of `anObject`, or `nil` if `object` is `nil` or if `object` could not be copied.

## Discussion

This function is deprecated and unavailable for use with ARC. To create a copy of an object, use the [copyWithZone:](../objectivec/nsobject-swift.class/copywithzone_.md) method instead.

## See Also

### Object Allocation and Deallocation

- [NSAllocateObject](nsallocateobject.md) — Creates and returns a new instance of a given class.
- [NSDeallocateObject](nsdeallocateobject.md) — Destroys an existing object.
- [NSDecrementExtraRefCountWasZero](nsdecrementextrarefcountwaszero.md) — Decrements the specified object’s reference count.
- [NSExtraRefCount](nsextrarefcount.md) — Returns the specified object’s reference count.
- [NSIncrementExtraRefCount](nsincrementextrarefcount.md) — Increments the specified object’s reference count.
- [NSShouldRetainWithZone](nsshouldretainwithzone.md) — Indicates whether an object should be retained.

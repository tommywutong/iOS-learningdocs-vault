---
title: NSAllocateCollectable
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsallocatecollectable
source_url: 'https://developer.apple.com/documentation/foundation/nsallocatecollectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsallocatecollectable.json'
content_hash: 'sha256:d9cdbe6c73144c1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAllocateCollectable

<sub>Function</sub>

Allocates collectable memory.

> [!warning] Deprecated
> Garbage collection is deprecated in OS X v10.8; instead,you should use AutomaticReference Counting—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

<sub>macOS</sub>

```objc
extern void *NSAllocateCollectable(NSUInteger size, NSUInteger options);
```

## Parameters

- `size` — The number of bytes of memory to allocate.

- `options` — `0` or `NSScannedOption`: A value of `0` allocates non-scanned memory; a value of `NSScannedOption` allocates scanned memory.

## Return Value

A pointer to the allocated memory, or `NULL` if the function is unable to allocate the requested memory.

## See Also

### Legacy

- [NSGarbageCollector](nsgarbagecollector.md) — A convenient interface to the garbage collection system. _(deprecated)_
- [NSReallocateCollectable](nsreallocatecollectable.md) — Reallocates collectable memory. _(deprecated)_
- [NSMakeCollectable](nsmakecollectable.md) — Makes a newly allocated Core Foundation object eligible for collection. _(deprecated)_
- [Memory Allocation Options](1539826-memory-allocation-options.md) — Constants used to control behavior when allocating or reallocating collectible memory.

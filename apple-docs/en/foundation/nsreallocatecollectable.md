---
title: NSReallocateCollectable
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsreallocatecollectable
source_url: 'https://developer.apple.com/documentation/foundation/nsreallocatecollectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsreallocatecollectable.json'
content_hash: 'sha256:1bceda45a5ec243f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSReallocateCollectable

<sub>Function</sub>

Reallocates collectable memory.

> [!warning] Deprecated
> Garbage collection is deprecated in OS X v10.8; instead,you should use AutomaticReference Counting—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

<sub>macOS</sub>

```objc
extern void *NSReallocateCollectable(void *ptr, NSUInteger size, NSUInteger options);
```

## Discussion

Changes the size of the block of memory pointed to by `ptr` to `size` bytes. It may allocate new memory to replace the old, in which case it moves the contents of the old memory block to the new block, up to a maximum of `size` bytes.

`options` can be `0` or `NSScannedOption`: A value of `0` allocates non-scanned memory; a value of `NSScannedOption` allocates scanned memory.

This function returns `NULL` if it’s unable to allocate the requested memory.

## See Also

### Legacy

- [NSGarbageCollector](nsgarbagecollector.md) — A convenient interface to the garbage collection system. _(deprecated)_
- [NSAllocateCollectable](nsallocatecollectable.md) — Allocates collectable memory. _(deprecated)_
- [NSMakeCollectable](nsmakecollectable.md) — Makes a newly allocated Core Foundation object eligible for collection. _(deprecated)_
- [Memory Allocation Options](1539826-memory-allocation-options.md) — Constants used to control behavior when allocating or reallocating collectible memory.

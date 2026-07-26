---
title: Memory Management Functions
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/memory-management-functions
source_url: 'https://developer.apple.com/documentation/foundation/memory-management-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/memory-management-functions.json'
content_hash: 'sha256:399f8a1e228d5045'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Object Runtime](object-runtime.md)

# Memory Management Functions

<sub>API Collection</sub>

Perform low-level memory management tasks.

## Topics

### Core Foundation ARC Integration

- [CFBridgingRetain](<cfbridgingretain(__).md>) — Casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to the caller.

### Memory Management

- [NSAllocateMemoryPages](<nsallocatememorypages(__).md>) — Allocates a new block of memory.
- [NSCopyMemoryPages](<nscopymemorypages(______).md>) — Copies a block of memory.
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — Deallocates the specified block of memory.
- [NSLogPageSize](<nslogpagesize().md>) — Returns the binary log of the page size.
- [NSPageSize](<nspagesize().md>) — Returns the number of bytes in a page.
- [NSRealMemoryAvailable](<nsrealmemoryavailable().md>) — Returns information about the user’s system. _(deprecated)_
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded down to a multiple of the page size.
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded up to a multiple of the page size.

## See Also

### Memory Management

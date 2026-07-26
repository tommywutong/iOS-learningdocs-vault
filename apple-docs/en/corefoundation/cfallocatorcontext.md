---
title: CFAllocatorContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorcontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcontext.json'
content_hash: 'sha256:5e13796f3e23460a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorContext

<sub>Structure</sub>

A structure that defines the context or operating environment for an allocator (CFAllocator) object. Every Core Foundation allocator object must have a context defined for it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFAllocatorContext
```

## Overview

See the [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i) topic for information on creating a custom CFAllocator object and, as part of that procedure, the steps for creating a properly initialized `CFAllocatorContext` structure.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfallocatorcontext/init().md>)
- [init(version:info:retain:release:copyDescription:allocate:reallocate:deallocate:preferredSize:)](<cfallocatorcontext/init(version_info_retain_release_copydescription_allocate_reallocate_deallocate_preferredsize_).md>)

### Instance Properties

- [allocate](cfallocatorcontext/allocate.md) — A prototype for a function callback that allocates memory of a requested size. In implementing this function, allocate a block of memory of at least `size` bytes and return a pointer to the start of the block. The `hint` argument is a bitfield that you should currently not use (that is, assign 0). The `size` parameter should always be greater than 0. If it is not, or if problems in allocation occur, return `NULL`. This function pointer may not be assigned `NULL`.
- [copyDescription](cfallocatorcontext/copydescription.md) — A prototype for a function callback that provides a description of the data pointed to by the `info` field. In implementing this function, return a reference to a CFString object that describes your allocator, particularly some characteristics of your program-defined data. You may set this function pointer to `NULL`, in which case Core Foundation will provide a rudimentary description.
- [deallocate](cfallocatorcontext/deallocate.md) — A prototype for a function callback that deallocates a given block of memory. In implementing this function, make the block of memory pointed to by `ptr` available for subsequent reuse by the allocator but unavailable for continued use by the program. The `ptr` parameter cannot be `NULL` and if the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. You can set this callback to `NULL`, in which case the [CFAllocatorDeallocate](<cfallocatordeallocate(____).md>) function has no effect.
- [info](cfallocatorcontext/info.md) — An untyped pointer to program-defined data. Allocate memory for this data and assign a pointer to it. This data is often control information for the allocator. You may assign `NULL`.
- [preferredSize](cfallocatorcontext/preferredsize.md) — A prototype for a function callback that determines whether there is enough free memory to satisfy a request. In implementing this function, return the actual size the allocator is likely to allocate given a request for a block of memory of size `size`. The `hint` argument is a bitfield that you should currently not use.
- [reallocate](cfallocatorcontext/reallocate.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [release](cfallocatorcontext/release.md) — A prototype for a function callback that releases the data pointed to by the `info` field. In implementing this function, release (or free) the data you have defined for the allocator context. You may set this function pointer to `NULL`, but doing so might result in memory leaks.
- [retain](cfallocatorcontext/retain.md) — A prototype for a function callback that retains the data pointed to by the `info` field. In implementing this function, retain the data you have defined for the allocator context in this field. (This might make sense only if the data is a Core Foundation object.) You may set this function pointer to `NULL`.
- [version](cfallocatorcontext/version.md) — An integer of type `CFIndex`. Assign the version number of the allocator. Currently the only valid value is 0.

---
title: CFAllocator
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocator
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocator.json'
content_hash: 'sha256:a6adc870efc631a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocator

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFAllocator
```

## Overview

CFAllocator is an opaque type that allocates and deallocates memory for you. You never have to allocate, reallocate, or deallocate memory directly for Core Foundation objects—and rarely should you. You pass CFAllocator objects into functions that create objects; these functions have “Create” embedded in their names, for example, `CFStringCreateWithPascalString`. The creation functions use the allocators to allocate memory for the objects they create.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating an Allocator

- [CFAllocatorCreate](<cfallocatorcreate(____).md>) — Creates an allocator object.

### Managing Memory with an Allocator

- [CFAllocatorAllocate](<cfallocatorallocate(______).md>) — Allocates memory using the specified allocator.
- [CFAllocatorDeallocate](<cfallocatordeallocate(____).md>) — Deallocates a block of memory with a given allocator.
- [CFAllocatorGetPreferredSizeForSize](<cfallocatorgetpreferredsizeforsize(______).md>) — Obtains the number of bytes likely to be allocated upon a specific request.
- [CFAllocatorReallocate](<cfallocatorreallocate(________).md>) — Reallocates memory using the specified allocator.

### Getting and Setting the Default Allocator

- [CFAllocatorGetDefault](<cfallocatorgetdefault().md>) — Gets the default allocator object for the current thread.
- [CFAllocatorSetDefault](<cfallocatorsetdefault(__).md>) — Sets the given allocator as the default for the current thread.

### Getting an Allocator’s Context

- [CFAllocatorGetContext](<cfallocatorgetcontext(____).md>) — Obtains the context of the specified allocator or of the default allocator.

### Getting the CFAllocator Type ID

- [CFAllocatorGetTypeID](<cfallocatorgettypeid().md>) — Returns the type identifier for the CFAllocator opaque type.

### Callbacks

- [CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md) — A prototype for a function callback that allocates memory of a requested size.
- [CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md) — A prototype for a function callback that provides a description of the specified data.
- [CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md) — A prototype for a function callback that deallocates a block of memory.
- [CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md) — A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md) — A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md) — A prototype for a function callback that releases the given data.
- [CFAllocatorRetainCallBack](cfallocatorretaincallback.md) — A prototype for a function callback that retains the given data.

### Data Types

- [CFAllocatorContext](cfallocatorcontext.md) — A structure that defines the context or operating environment for an allocator (CFAllocator) object. Every Core Foundation allocator object must have a context defined for it.

### Constants

- [Predefined Allocators](predefined-allocators.md) — CFAllocator provides the following predefined allocators. In general, you should use `kCFAllocatorDefault` unless one of the special circumstances exist below.

## See Also

### Related Documentation

- [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)

### Opaque Types

- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

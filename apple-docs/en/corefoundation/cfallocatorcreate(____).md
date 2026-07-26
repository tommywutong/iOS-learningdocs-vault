---
title: 'CFAllocatorCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfallocatorcreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcreate%28_%3A_%3A%29.json'
content_hash: 'sha256:efce870f0ca097e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorCreate(_:_:)

<sub>Function</sub>

Creates an allocator object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorCreate(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!) -> Unmanaged<CFAllocator>!
```

## Parameters

- `allocator` — The existing allocator to use to allocate memory for the new allocator. Pass the [kCFAllocatorUseContext](kcfallocatorusecontext.md) constant for this parameter to allocate memory using the appropriate function callback specified in the `context` parameter. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to allocate memory for the new allocator using the default allocator.

- `context` — A structure of type [CFAllocatorContext](cfallocatorcontext.md). The fields of this structure hold (among other things) function pointers to callbacks used for allocating, reallocating, and deallocating memory.

## Return Value

The new allocator object, or `NULL` if there was a problem allocating memory. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You use this function to create custom allocators which you can then pass into various Core Foundation object-creation functions. You must implement a function callback that allocates memory and assign it to the `allocate` field of this structure. You typically also implement deallocate, reallocate, and preferred-size callbacks.

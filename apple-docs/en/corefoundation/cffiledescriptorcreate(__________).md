---
title: 'CFFileDescriptorCreate(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorcreate(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorcreate(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorcreate%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:058e2341af4f3bef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorCreate(_:_:_:_:_:)

<sub>Function</sub>

Creates a new CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Bool, _ callout: CFFileDescriptorCallBack!, _ context: UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new file descriptor object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `fd` — The file descriptor for the new CFFileDescriptor.

- `closeOnInvalidate` — `true` if the new CFFileDescriptor should close `fd` when it is invalidated, otherwise `false`.

- `callout` — The CFFileDescriptorCallBack for the new CFFileDescriptor.

- `context` — Contextual information for the new CFFileDescriptor.

## Return Value

A new CFFileDescriptor or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Related Documentation

- [CFFileDescriptorGetContext](<cffiledescriptorgetcontext(____).md>) — Gets the context for a given CFFileDescriptor.
- [CFFileDescriptorInvalidate](<cffiledescriptorinvalidate(__).md>) — Invalidates a CFFileDescriptor object.

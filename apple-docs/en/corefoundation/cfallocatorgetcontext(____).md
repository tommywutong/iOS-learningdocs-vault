---
title: 'CFAllocatorGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfallocatorgetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorgetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorgetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:22d20a7788323859'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorGetContext(_:_:)

<sub>Function</sub>

Obtains the context of the specified allocator or of the default allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!)
```

## Parameters

- `allocator` — The allocator to examine. Pass `NULL` to obtain the context of the default allocator.

- `context` — On return, contains the context of `allocator`.

## Discussion

An allocator’s context, a structure of type `CFAllocatorContext`, holds pointers to various function callbacks (particularly those that allocate, reallocate, and deallocate memory for an object). The context also contains a version number and the `info` field for program-defined data. To obtain the value of the `info` field you usually first have to get an allocator’s context.

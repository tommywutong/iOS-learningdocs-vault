---
title: 'CFTreeCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cftreecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:ed0b9638bd0c2490'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeCreate(_:_:)

<sub>Function</sub>

Creates a new CFTree object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFTreeCreate(_ allocator: CFAllocator!, _ context: UnsafePointer<CFTreeContext>!) -> CFTree!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new tree. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `context` — The [CFTreeContext](cftreecontext.md) structure to be copied and used as the context of the new tree. The information pointer will be retained by the tree if a retain function is provided. If this value is not a valid C pointer to a [CFTreeContext](cftreecontext.md) structure-sized block of storage, the result is undefined. If the version number of the storage is not a valid [CFTreeContext](cftreecontext.md) version number, the result is undefined.

## Return Value

A new CFTree object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

---
title: 'CFFileDescriptorCreateRunLoopSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cffiledescriptorcreaterunloopsource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cffiledescriptorcreaterunloopsource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffiledescriptorcreaterunloopsource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3c25ecaff633f7b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileDescriptorCreateRunLoopSource(_:_:_:)

<sub>Function</sub>

Creates a new runloop source for a given CFFileDescriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFFileDescriptorCreateRunLoopSource(_ allocator: CFAllocator!, _ f: CFFileDescriptor!, _ order: CFIndex) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bag and its storage for values. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `f` — A CFFileDescriptor.

- `order` — The order for the new run loop (see [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>)).

## Return Value

A new runloop source for `f`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The context for the new runloop (see [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>)) is the same as the context passed in when the CFFileDescriptor was created (see [CFFileDescriptorCreate](<cffiledescriptorcreate(__________).md>)).

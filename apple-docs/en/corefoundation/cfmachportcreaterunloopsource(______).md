---
title: 'CFMachPortCreateRunLoopSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportcreaterunloopsource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcreaterunloopsource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcreaterunloopsource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9ea6d484360d2d90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortCreateRunLoopSource(_:_:_:)

<sub>Function</sub>

Creates a CFRunLoopSource object for a CFMachPort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortCreateRunLoopSource(_ allocator: CFAllocator!, _ port: CFMachPort!, _ order: CFIndex) -> CFRunLoopSource!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `port` — The Mach port for which to create a CFRunLoopSource object.

- `order` — A priority index indicating the order in which run loop sources are processed. `order` is currently ignored by CFMachPort run loop sources. Pass `0` for this value.

## Return Value

The new CFRunLoopSource object for `port`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The run loop source is not automatically added to a run loop. To add the source to a run loop, use [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

## See Also

### Configuring a CFMachPort Object

- [CFMachPortInvalidate](<cfmachportinvalidate(__).md>) — Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMachPort object is invalidated.

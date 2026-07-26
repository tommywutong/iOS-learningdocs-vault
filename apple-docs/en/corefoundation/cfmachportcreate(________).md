---
title: 'CFMachPortCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportcreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:23da2f03c23cb149'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortCreate(_:_:_:_:)

<sub>Function</sub>

Creates a CFMachPort object with a new Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortCreate(_ allocator: CFAllocator!, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `callout` — The callback function invoked when a message is received on the new Mach port.

- `context` — A structure holding contextual information for the new Mach port. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call.

- `shouldFreeInfo` — A flag set by the function to indicate whether the `info` member of `context` should be freed. The flag is set to `true` on failure, `false` otherwise. `shouldFreeInfo` can be `NULL`.

## Return Value

The new CFMachPort object or `NULL` on failure. The CFMachPort object has both send and receive rights. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFMachPort Object

- [CFMachPortCreateWithPort](<cfmachportcreatewithport(__________).md>) — Creates a CFMachPort object for a pre-existing native Mach port.

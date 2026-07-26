---
title: 'CFMachPortCreateWithPort(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportcreatewithport(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcreatewithport(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcreatewithport%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9360e1a70174f42b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortCreateWithPort(_:_:_:_:_:)

<sub>Function</sub>

Creates a CFMachPort object for a pre-existing native Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortCreateWithPort(_ allocator: CFAllocator!, _ portNum: mach_port_t, _ callout: CFMachPortCallBack!, _ context: UnsafeMutablePointer<CFMachPortContext>!, _ shouldFreeInfo: UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `portNum` — The native Mach port to use.

- `callout` — The callback function invoked when a message is received on the Mach port.

- `context` — A structure holding contextual information for the Mach port. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call.

- `shouldFreeInfo` — A flag set by the function to indicate whether the `info` member of `context` should be freed. The flag is set to `true` on failure or if a CFMachPort object already exists for `portNum`, `false` otherwise. `shouldFreeInfo` can be `NULL`.

## Return Value

The new CFMachPort object or `NULL` on failure. If a CFMachPort object already exists for `portNum`, the function returns the pre-existing object instead of creating a new object; the `context` and `callout` parameters are ignored in this case. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The CFMachPort object does not take full ownership of the send and receive rights of the Mach port `portNum`. It is the caller’s responsibility to deallocate the Mach port rights after the CFMachPort object is no longer needed and has been invalidated.

## See Also

### Creating a CFMachPort Object

- [CFMachPortCreate](<cfmachportcreate(________).md>) — Creates a CFMachPort object with a new Mach port.

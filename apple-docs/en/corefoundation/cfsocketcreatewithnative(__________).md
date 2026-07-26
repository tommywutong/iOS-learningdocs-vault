---
title: 'CFSocketCreateWithNative(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcreatewithnative(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcreatewithnative(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcreatewithnative%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:34091d315f07079a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCreateWithNative(_:_:_:_:_:)

<sub>Function</sub>

Creates a CFSocket object for a pre-existing native socket.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCreateWithNative(_ allocator: CFAllocator!, _ sock: CFSocketNativeHandle, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `sock` — The native socket for which to create a CFSocket object.

- `callBackTypes` — A bitwise-OR combination of the types of socket activity that should cause `callout` to be called. See [CFSocketCallBackType](cfsocketcallbacktype.md) for the possible activity values.

- `callout` — The function to call when one of the activities indicated by `callBackTypes` occurs.

- `context` — A structure holding contextual information for the CFSocket object. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call. Can be `NULL`.

## Return Value

The new CFSocket object, or `NULL` if an error occurred. If a CFSocket object already exists for `sock`, the function returns the pre-existing object instead of creating a new object; the `context`, `callout`, and `callBackTypes` parameters are ignored in this case. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Sockets

- [CFSocketCreate](<cfsocketcreate(______________).md>) — Creates a CFSocket object of a specified protocol and type.
- [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>) — Creates a CFSocket object and opens a connection to a remote socket.
- [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>) — Creates a CFSocket object using information from a CFSocketSignature structure.

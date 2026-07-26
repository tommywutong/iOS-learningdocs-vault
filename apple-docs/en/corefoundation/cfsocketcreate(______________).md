---
title: 'CFSocketCreate(_:_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcreate(_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcreate(_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcreate%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a84be2247cc82438'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCreate(_:_:_:_:_:_:_:)

<sub>Function</sub>

Creates a CFSocket object of a specified protocol and type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCreate(_ allocator: CFAllocator!, _ protocolFamily: Int32, _ socketType: Int32, _ protocol: Int32, _ callBackTypes: CFOptionFlags, _ callout: CFSocketCallBack!, _ context: UnsafePointer<CFSocketContext>!) -> CFSocket!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `protocolFamily` — The protocol family for the socket. If negative or 0 is passed, the socket defaults to `PF_INET`.

- `socketType` — The socket type to create. If `protocolFamily` is `PF_INET` and `socketType` is negative or 0, the socket type defaults to `SOCK_STREAM`.

- `protocol` — The protocol for the socket. If `protocolFamily` is `PF_INET` and `protocol` is negative or 0, the socket protocol defaults to `IPPROTO_TCP` if `socketType` is `SOCK_STREAM` or `IPPROTO_UDP` if `socketType` is `SOCK_DGRAM`.

- `callBackTypes` — A bitwise-OR combination of the types of socket activity that should cause `callout` to be called. See [CFSocketCallBackType](cfsocketcallbacktype.md) for the possible activity values.

- `callout` — The function to call when one of the activities indicated by `callBackTypes` occurs.

- `context` — A structure holding contextual information for the CFSocket object. The function copies the information out of the structure, so the memory pointed to by `context` does not need to persist beyond the function call. Can be `NULL`.

## Return Value

The new CFSocket object, or `NULL` if an error occurred. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Sockets

- [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>) — Creates a CFSocket object and opens a connection to a remote socket.
- [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>) — Creates a CFSocket object for a pre-existing native socket.
- [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>) — Creates a CFSocket object using information from a CFSocketSignature structure.

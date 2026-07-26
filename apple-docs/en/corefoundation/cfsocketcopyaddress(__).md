---
title: 'CFSocketCopyAddress(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcopyaddress(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcopyaddress(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcopyaddress%28_%3A%29.json'
content_hash: 'sha256:89951316cc41b00e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCopyAddress(_:)

<sub>Function</sub>

Returns the local address of a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCopyAddress(_ s: CFSocket!) -> CFData!
```

## Parameters

- `s` — The CFSocket object to examine.

## Return Value

The local address, stored as a `struct sockaddr` appropriate for the protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example) in a CFData object, of `s`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Configuring Sockets

- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

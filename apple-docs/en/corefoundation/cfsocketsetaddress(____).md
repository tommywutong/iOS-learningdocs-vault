---
title: 'CFSocketSetAddress(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketsetaddress(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsetaddress(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsetaddress%28_%3A_%3A%29.json'
content_hash: 'sha256:070b8e2e6057112d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketSetAddress(_:_:)

<sub>Function</sub>

Binds a local address to a CFSocket object and configures it for listening.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketSetAddress(_ s: CFSocket!, _ address: CFData!) -> CFSocketError
```

## Parameters

- `s` — The CFSocket object to modify.

- `address` — A CFData object containing a `struct sockaddr` appropriate for the protocol family of `s` (`struct sockaddr_in` or `struct sockaddr_in6`, for example). This data object is used only for the duration of the function call.

## Return Value

An error code indicating success or failure.

## Discussion

This function binds the socket by calling bind, and if the socket supports it, configures the socket for listening by calling listen with a backlog of 256.

Once `s` is bound to `address`, depending on the socket’s protocol, other processes and computers can connect to `s`.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

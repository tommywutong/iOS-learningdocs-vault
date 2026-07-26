---
title: 'CFSocketEnableCallBacks(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketenablecallbacks(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketenablecallbacks(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketenablecallbacks%28_%3A_%3A%29.json'
content_hash: 'sha256:4908d9a6fff54945'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketEnableCallBacks(_:_:)

<sub>Function</sub>

Enables the callback function of a CFSocket object for certain types of socket activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketEnableCallBacks(_ s: CFSocket!, _ callBackTypes: CFOptionFlags)
```

## Parameters

- `s` — The CFSocket object to modify.

- `callBackTypes` — A bitwise-OR combination of CFSocket activity types that should cause the callback function of `s` to be called. See [CFSocketCallBackType](cfsocketcallbacktype.md) for a list of callback types.

## Discussion

If a callback type is not automatically reenabled, you can use this function to enable the callback (once).

This call does not affect whether the callback type will be automatically reenabled in the future; use [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) if you want to set a callback type to be reenabled automatically.

Be sure to enable only callback types that your CFSocket object actually possesses and has requested when creating the CFSocket object; the result of enabling other callback types is undefined.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

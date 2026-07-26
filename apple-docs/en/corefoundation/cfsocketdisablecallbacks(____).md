---
title: 'CFSocketDisableCallBacks(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketdisablecallbacks(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketdisablecallbacks(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketdisablecallbacks%28_%3A_%3A%29.json'
content_hash: 'sha256:3ff28bfd7740c70e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketDisableCallBacks(_:_:)

<sub>Function</sub>

Disables the callback function of a CFSocket object for certain types of socket activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketDisableCallBacks(_ s: CFSocket!, _ callBackTypes: CFOptionFlags)
```

## Parameters

- `s` — The CFSocket object to modify.

- `callBackTypes` — A bitwise-OR combination of CFSocket activity types that should not cause the callback function of `s` to be called. See [CFSocketCallBackType](cfsocketcallbacktype.md) for a list of callback types.

## Discussion

If you no longer want certain types of callbacks that you requested when creating `s`, you can use this function to temporarily disable the callback. Use [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) to reenable a callback type.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

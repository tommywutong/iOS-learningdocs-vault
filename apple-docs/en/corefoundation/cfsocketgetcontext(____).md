---
title: 'CFSocketGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketgetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketgetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketgetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:e51a1c1c6bafeed3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketGetContext(_:_:)

<sub>Function</sub>

Returns the context information for a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketGetContext(_ s: CFSocket!, _ context: UnsafeMutablePointer<CFSocketContext>!)
```

## Parameters

- `s` — The CFSocket object to examine.

- `context` — A pointer to the structure into which the context information for `s` is to be copied. The information being returned is usually the same information you passed to [CFSocketCreate](<cfsocketcreate(______________).md>), [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>), [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>), or [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>) when creating the CFSocket object. However, if [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>) returned a cached CFSocket object instead of creating a new object, `context` is filled with information from the original CFSocket object instead of the information you passed to the function.

## Discussion

The context version number for CFSocket is currently 0. Before calling this function, you need to initialize the `version` member of `context` to 0.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

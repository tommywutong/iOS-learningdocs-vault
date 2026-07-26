---
title: 'CFSocketGetSocketFlags(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketgetsocketflags(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketgetsocketflags(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketgetsocketflags%28_%3A%29.json'
content_hash: 'sha256:2c7f87aabc8be624'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketGetSocketFlags(_:)

<sub>Function</sub>

Returns flags that control certain behaviors of a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketGetSocketFlags(_ s: CFSocket!) -> CFOptionFlags
```

## Parameters

- `s` — The CFSocket to examine.

## Return Value

A bitwise-OR combination of flags controlling the behavior of `s`. See [CFSocket Flags](1560944-cfsocket-flags.md) for the list of available flags.

## Discussion

See [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) for details on what the flags of a CFSocket mean.

## See Also

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

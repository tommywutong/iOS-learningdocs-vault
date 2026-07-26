---
title: CFSocketCallBackType
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcallbacktype
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcallbacktype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcallbacktype.json'
content_hash: 'sha256:7ed520bfd8b2d493'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCallBackType

<sub>Structure</sub>

Types of socket activity that can cause the callback function of a CFSocket object to be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFSocketCallBackType
```

## Overview

The callback types for which a callback is made is determined when the CFSocket object is created, such as with [CFSocketCreate](<cfsocketcreate(______________).md>), or later with [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) and [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>).

The `kCFSocketReadCallBack`, `kCFSocketAcceptCallBack`, and `kCFSocketDataCallBack` callbacks are mutually exclusive.

### Version-Notes

`kCFSocketWriteCallBack` is available in macOS 10.2 and later.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFSocketReadCallBack](cfsocketcallbacktype/readcallback.md) — The callback is called when data is available to be read or a new connection is waiting to be accepted. The data is not automatically read; the callback must read the data itself.
- [kCFSocketAcceptCallBack](cfsocketcallbacktype/acceptcallback.md) — New connections will be automatically accepted and the callback is called with the data argument being a pointer to a [CFSocketNativeHandle](cfsocketnativehandle.md) of the child socket. This callback is usable only with listening sockets.
- [kCFSocketDataCallBack](cfsocketcallbacktype/datacallback.md) — Incoming data will be read in chunks in the background and the callback is called with the data argument being a CFData object containing the read data.
- [kCFSocketConnectCallBack](cfsocketcallbacktype/connectcallback.md)
- [kCFSocketWriteCallBack](cfsocketcallbacktype/writecallback.md) — The callback is called when the socket is writable. This callback type may be useful when large amounts of data are being sent rapidly over the socket and you want a notification when there is space in the kernel buffers for more data.

### Initializers

- [init(rawValue:)](<cfsocketcallbacktype/init(rawvalue_).md>)

## See Also

### Constants

- [CFSocket Flags](1560944-cfsocket-flags.md) — Flags that can be set on a CFSocket object to control its behavior.
- [CFSocketError](cfsocketerror.md) — Error codes for many CFSocket functions.
